# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from currency_app.models import Rate
from scrapy_djangoitem import DjangoItem

#contrib.djangoitem import DjangoItem

class ScraperItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    model = Rate

