from abc import ABC

import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        contents = response.css('div.quote')

        for content in contents:
            theword = content.css('.text::text').get()
            author = content.css('.author::text').get()
            tags = content.css('a.tag::text').getall()

            yield {
                'content': theword,
                'author': author,
                'tags': tags,
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
