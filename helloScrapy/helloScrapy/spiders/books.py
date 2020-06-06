# -*- coding: utf-8 -*-
import scrapy
from environs import Env
from helloScrapy.items import BookItem
from icecream import ic

env = Env()
env.read_env()

InCrontab = env.bool("InCrontab", False)


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['http://books/']
    if InCrontab:
        pipeline = 'helloScrapy.pipelines.CrontabBooksPipeline'
        start_urls = [
            'https://www.shudan.vip/page/1',
            # *[f'http://www.zxcs.me/sort/{i}' for i in [23, *list(range(25, 30)), *list(range(36, 46)), 55]],
            *[f'http://www.java1234.com{i}' for i in '''/a/javabook/javabase/
            /a/javabook/database/
            /a/javabook/webbase/
            /a/javabook/javaweb/
            /a/javabook/andriod/
            /a/javabook/yun/
            /a/javabook/blockchain/
            /a/javabook/newBook/'''.split()],
            *[f'http://www.mianhuatang.cc/mulu/{i}-1.html' for i in range(1, 11)]
        ]
    else:
        pipeline = 'helloScrapy.pipelines.BooksPipeline'
        start_urls = [
            # *[f'http://www.mianhuatang.cc/mulu/1-{i}.html' for i in range(1, 1104 + 1)],
            # *[f'http://www.mianhuatang.cc/mulu/2-{i}.html' for i in range(1, 330 + 1)],
            # *[f'http://www.mianhuatang.cc/mulu/3-{i}.html' for i in range(1, 1202 + 1)],
            # *[f'http://www.mianhuatang.cc/mulu/4-{i}.html' for i in range(1, 415 + 1)],
            # *[f'http://www.mianhuatang.cc/mulu/5-{i}.html' for i in range(1, 141 + 1)],
            # *[f'http://www.mianhuatang.cc/mulu/6-{i}.html' for i in range(1, 363 + 1)],
            # *[f'http://www.mianhuatang.cc/mulu/7-{i}.html' for i in range(1, 297 + 1)],
            # *[f'http://www.mianhuatang.cc/mulu/8-{i}.html' for i in range(1, 230 + 1)],
            # *[f'http://www.mianhuatang.cc/mulu/9-{i}.html' for i in range(1, 409 + 1)],
            # *[f'http://www.mianhuatang.cc/mulu/10-{i}.html' for i in range(1, 1455 + 1)],
        ]
    ic(start_urls)

    xpath = {
        'www.shudan.vip': {
            'urlsXpath': "//h2[@class='block-title']/a/@href",
            'namesXpath': "//h2[@class='block-title']/a/text()"
        },
        'www.zxcs.me': {
            'urlsXpath': "//dl[@id='plist']/dt/a/@href",
            'namesXpath': "//dl[@id='plist']/dt/a/text()"
        },
        'www.java1234.com': {
            'urlsXpath': "//div[@class='listbox']/ul[@class='e2']/li/a[@class='title']/@href",
            'namesXpath': "//div[@class='listbox']/ul[@class='e2']/li/a[@class='title']/text()"
        },
        'www.mianhuatang.cc': {
            'urlsXpath': "//div[@class='title']/h2/a/@href",
            'namesXpath': "//div[@class='title']/h2/a/text()"
        }
    }

    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 0,
        'DOWNLOAD_TIMEOUT': 10,
        'ITEM_PIPELINES': {pipeline: 300},
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
