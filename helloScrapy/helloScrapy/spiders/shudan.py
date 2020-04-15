# -*- coding: utf-8 -*-
import scrapy

from helloScrapy.items import BookItem


class ShudanSpider(scrapy.Spider):
    name = 'shudan'
    allowed_domains = ['shudan.vip', 'pan.shudan.vip']
    start_urls = [f'https://pan.shudan.vip/page/{i}' for i in range(1, 749)]
#     start_urls.extend(f'https://pan.shudan.vip/page/{i}' for i in range(1, 749))
    custom_settings = {
        'ITEM_PIPELINES': {'helloScrapy.pipelines.ShudanPipeline': 300},
    }

    def parse(self, response):
        books = response.css('.block-title a')
        for book in books:
            item = BookItem()
            item['book_url'] = book.css('::attr(href)').extract_first()
            item['book_name'] = book.css('::text').extract_first()
            yield item
