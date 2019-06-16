import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = "logo"

    def start_requests(self):
        urls = [
            'https://www.metal-archives.com/browse/ajax-genre/g/black/json/1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        json_response = json.loads(response.body_as_unicode())

        print(json_response)
        
