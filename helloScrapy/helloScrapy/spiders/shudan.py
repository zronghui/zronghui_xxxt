# -*- coding: utf-8 -*-
import scrapy

from helloScrapy.items import BookItem


class ShudanSpider(scrapy.Spider):
    name = 'shudan'
    allowed_domains = ['shudan.vip', 'pan.shudan.vip']
    start_urls = [f'https://www.shudan.vip/page/{i}' for i in range(1, 150)]
    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
        'ITEM_PIPELINES': {'helloScrapy.pipelines.ShudanPipeline': 300},
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'
        },
    }

    def parse(self, response):
        #
        urls = response.xpath("//h2[@class='block-title']/a/@href").extract()
        names = response.xpath("//h2[@class='block-title']/a/text()").extract()
        for url, name in zip(urls, names):
            item = BookItem()
            item['book_url'] = url
            item['book_name'] = name
            yield item
        # books = response.css('.block-title a')
        # for book in books:
        #     item = BookItem()
        #     item['book_url'] = book.css('::attr(href)').extract_first()
        #     item['book_name'] = book.css('::text').extract_first()
        #     yield item
