# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonSpiderItem


class AmazonWebspiderSpider(scrapy.Spider):
    name = 'amazon_webspider'
    start_urls = [
        'https://www.amazon.com/s?k=python&i=stripbooks&ref=nb_sb_noss_2'
    ]

    def parse(self, response):
        pass
