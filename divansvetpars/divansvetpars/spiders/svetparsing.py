import scrapy


class SvetparsingSpider(scrapy.Spider):
    name = "svetparsing"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru"]

    def parse(self, response):
        pass
