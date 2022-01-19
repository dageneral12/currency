from django.db import models
from currency_app import modelchoices as mch


class Source(models.Model):

    id = models.IntegerField(primary_key=True) # noqa
    name = models.CharField(max_length=64, unique=True)
    source_url = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name


class Rate(models.Model):

    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    source = models.ForeignKey(Source, to_field='name',
                               on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, choices=mch.RATE_CHOICES)
# Use rate.get_currency_diplay in template
# to display 'human' values from choices
# get_{attribute_name}_display - is the format
    created = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):

    id = models.IntegerField(primary_key=True) # noqa
    email_from = models.CharField(max_length=24)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)


class ResponseLog(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    status_code = models.PositiveIntegerField()
    path = models.CharField(max_length=255)
    response_time = models.PositiveIntegerField(help_text='In milliseconds') # noqa
    request_methods = models.CharField(max_length=10,
                                       choices=mch.REQUEST_METHODS,
                                       default='GET')
