import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import FirstWebSpiderItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'crsf_token': token,
            'username': '123123@123.com',
            'password': '123123'
        }, callback = self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
        items = FirstWebSpiderItem()

        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:

            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
