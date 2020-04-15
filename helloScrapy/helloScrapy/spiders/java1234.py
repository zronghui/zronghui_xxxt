# -*- coding: utf-8 -*-
import scrapy

from helloScrapy.items import BookItem


class Java1234Spider(scrapy.Spider):
    name = 'java1234'
    allowed_domains = ['www.java1234.com']
    start_urls = [f'http://www.java1234.com{i}' for i in '''/a/javabook/javabase/
/a/javabook/database/
/a/javabook/webbase/
/a/javabook/javaweb/
/a/javabook/andriod/
/a/javabook/yun/
/a/javabook/blockchain/
/a/javabook/newBook/'''.split()]

    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
        'ITEM_PIPELINES': {'helloScrapy.pipelines.Java1234Pipeline': 300},
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'
        },
    }

    def parse(self, response):
        try:
            pages = response.xpath("//ul[@class='pagelist']/li/a/@href").extract()
            for page in pages:
                if response.url.endswith('html'):
                    yield scrapy.Request(url=f'{response.url.rsplit("/", 1)[0]}/{page}', callback=self.parse)
                else:
                    yield scrapy.Request(url=f'{response.url}{page}', callback=self.parse)
            urls = response.xpath("//div[@class='listbox']/ul[@class='e2']/li/a[@class='title']/@href").extract()
            names = response.xpath("//div[@class='listbox']/ul[@class='e2']/li/a[@class='title']/text()").extract()
            for i in range(len(urls)):
                item = BookItem()
                item['book_url'] = f'http://www.java1234.com{urls[i]}'
                item['book_name'] = names[i]
                yield item

        except Exception as e:
            print(e)
            return
