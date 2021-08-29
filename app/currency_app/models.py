from django.db import models


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
                               on_delete=models.CASCADE,
                               default=1)
    currency = models.CharField(max_length=3)


class ContactUs(models.Model):

    id = models.IntegerField(primary_key=True) # noqa
    email_from = models.CharField(max_length=24)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)


