# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonSpiderItem


class AmazonWebspiderSpider(scrapy.Spider):
    name = 'amazon_webspider'
    start_urls = [
        'https://www.amazon.com/s?k=python&i=stripbooks&ref=nb_sb_noss_2'
    ]

    def parse(self, response):
        items = AmazonSpiderItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price:nth-child(1) span').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()
        product_review = response.css('.a-size-small .a-size-base').css('::text').extract()
        product_rating = response.css('.a-icon-alt::text').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink
        items['product_review'] = product_review
        items['product_rating'] = product_rating

        yield items
