# -*- coding: utf-8 -*-
import scrapy
from icecream import ic

from helloScrapy.items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['http://books/']
    start_urls = [
        *[f'http://www.zxcs.me/sort/{i}' for i in [23, *list(range(25, 30)), *list(range(36, 46)), 55]],
        *[f'http://www.java1234.com{i}' for i in '''/a/javabook/javabase/
            /a/javabook/database/
            /a/javabook/webbase/
            /a/javabook/javaweb/
            /a/javabook/andriod/
            /a/javabook/yun/
            /a/javabook/blockchain/
            /a/javabook/newBook/'''.split()],
    ]
    ic(start_urls)

    xpath = {
        'www.zxcs.me': {
            'urlsXpath': "//dl[@id='plist']/dt/a/@href",
            'namesXpath': "//dl[@id='plist']/dt/a/text()"
        },
        'www.java1234.com': {
            'urlsXpath': "//div[@class='listbox']/ul[@class='e2']/li/a[@class='title']/@href",
            'namesXpath': "//div[@class='listbox']/ul[@class='e2']/li/a[@class='title']/text()"
        }
    }

    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
        'ITEM_PIPELINES': {'helloScrapy.pipelines.BooksPipeline': 300},
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'
        },
    }

    def parse(self, response):
        domain = response.url.split('/', 3)[2]
        httpDomain = '/'.join(response.url.split('/', 3)[:3])
        ic(response.url, domain, httpDomain)
        urls = response.xpath(self.xpath[domain]["urlsXpath"]).extract()
        names = response.xpath(self.xpath[domain]["namesXpath"]).extract()
        ic(len(urls))
        if len(urls) > 0 and urls[0].startswith('/'):
            urls = [httpDomain + i for i in urls]
        for url, name in zip(urls, names):
            item = BookItem()
            item['book_url'] = url
            item['book_name'] = name
            yield item
