# -*- coding: utf-8 -*-
import scrapy

from helloScrapy.items import BookItem


class ItsckSpider(scrapy.Spider):
    name = 'itsck'
    allowed_domains = ['www.itsck.com']
    start_urls = [f'https://www.itsck.com/type/{i}.html' for i in
                  ['dianying', 'lianxuju', 'zongyi', 'dongman']
                  ]
    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
        'ITEM_PIPELINES': {'helloScrapy.pipelines.ItsckPipeline': 300},
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'
        },
    }

    def parse(self, response):
        try:
            pages = response.xpath("//a[@class='fed-btns-info fed-rims-info']/@href").extract()
            for page in pages:
                yield scrapy.Request(url=f'https://www.itsck.com{page}', callback=self.parse)
            urls = response.xpath("//a[@class='fed-list-title fed-font-xiv fed-text-center "
                                  "fed-text-sm-left fed-visible fed-part-eone']/@href").extract()
            names = response.xpath("//a[@class='fed-list-title fed-font-xiv fed-text-center "
                                   "fed-text-sm-left fed-visible fed-part-eone']/text()").extract()
            for i in range(len(urls)):
                item = BookItem()
                item['book_url'] = f'https://www.itsck.com{urls[i]}'
                item['book_name'] = names[i]
                yield item

        except Exception as e:
            print(e)
            return
