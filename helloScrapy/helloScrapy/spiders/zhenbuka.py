# -*- coding: utf-8 -*-
import scrapy

from helloScrapy.items import BookItem


class ZhenbukaSpider(scrapy.Spider):
    name = 'zhenbuka'
    allowed_domains = ['www.zhenbuka.com']
    start_urls = [f'https://www.zhenbuka.com/vodtype/{i}' for i in range(1, 5)]
    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
        'ITEM_PIPELINES': {'helloScrapy.pipelines.ZhenbukaPipeline': 300},
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'
        },
    }

    def parse(self, response):
        try:
            pages = response.xpath("//ul[@class='stui-page text-center clearfix']/li/a/@href") \
                .extract()
            for page in list(set(pages)):
                yield scrapy.Request(url=f'https://www.zhenbuka.com{page}', callback=self.parse)
            urls = response.xpath("//h4[@class='title text-overflow']/a/@href").extract()
            names = response.xpath("//h4[@class='title text-overflow']/a/text()").extract()
            for i in range(len(urls)):
                item = BookItem()
                item['book_url'] = f'https://www.zhenbuka.com{urls[i]}'
                item['book_name'] = names[i]
                yield item

        except Exception as e:
            print(e)
            return

