# -*- coding: utf-8 -*-
import scrapy

from helloScrapy.items import BookItem


class BttwoSpider(scrapy.Spider):
    name = 'bttwo'
    allowed_domains = ['www.bttwo.com']
    start_urls = [f'https://www.bttwo.com/new-movie/page/{i}' for i in range(1, 83)]
    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
        'ITEM_PIPELINES': {'helloScrapy.pipelines.BttwoPipeline': 300},
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'
        },
    }

    def parse(self, response):
        try:
            urls = response.xpath("//h3[@class='dytit']/a/@href").extract()
            names = response.xpath("//h3[@class='dytit']/a/text()").extract()
            for i in range(len(urls)):
                item = BookItem()
                item['book_url'] = urls[i]
                item['book_name'] = names[i]
                yield item
        except Exception as e:
            print(e)
            return
