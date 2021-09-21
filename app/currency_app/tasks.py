from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from currency_app import modelchoices as mch
# app = Celery('tasks', broker='amqp://localhost')


def round_currency(amount):

    from decimal import Decimal
    return Decimal(amount).quantize(Decimal('0.01'))


# run 'debug_task.delay() to run the task
# through the celery Worker (asynchronously)

# run debug_task.apply_async(args=[1], kwargs = {'sleep_time': 3}, countdown=100) # noqa
# can use args/kwargs, countdown for delayed execution

# this is a decorator indicating that it's a workers task

@shared_task
def debug_task(sleep_time: int = 5):
    from time import sleep
    sleep_time = 5
    sleep(sleep_time)


@shared_task
def parse_privat_bank():
    import requests
    import datetime
    from currency_app.models import Rate, Source
    PARSE_API = \
        'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    response = requests.get(PARSE_API)
    response.raise_for_status()
    source = Source.objects.filter(name='Privatbank')
    rates = response.json(response)
    available_currency_rates = [mch.RATE_CHOICES[x][0] for x in range(len(mch.RATE_CHOICES))] # noqa
    for rate in rates:
        if rate['ccy'].upper() in available_currency_rates:
            currency_type = rate['ccy']
            sale = round_currency(rate['sale'])
            buy = round_currency(rate['buy'])
            created = datetime.datetime.now()

            last_rate = Rate.objects.filter(
                currency=currency_type,
                source=source
            ).order_by('created').last()

            if (last_rate.sale is not None
                    or last_rate != sale
                    or last_rate.buy != buy):
                Rate.objects.create(
                    source=source,
                    sale=sale,
                    buy=buy,
                    currency=currency_type,
                    created=created
                    )


@shared_task
def send_emails(subject, body):
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.SUPPORT_EMAIL],
        fail_silently=False
    )
