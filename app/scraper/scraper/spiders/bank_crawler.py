import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'bank_crawler'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
