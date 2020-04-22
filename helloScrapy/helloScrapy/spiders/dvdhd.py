# -*- coding: utf-8 -*-
import scrapy

from helloScrapy.items import BookItem


class DvdhdSpider(scrapy.Spider):
    name = 'dvdhd'
    allowed_domains = ['dvdhd.me']
    start_urls = [f'https://dvdhd.me/list/index{i}.html' for i in range(1, 6)]
    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
        'ITEM_PIPELINES': {'helloScrapy.pipelines.DvdhdPipeline': 300},
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'
        },
    }

    def parse(self, response):
        try:
            pages = response.xpath("//div[@class='pagination pagination-multi']/ul/li/a/@href") \
                .extract()
            for page in pages:
                yield scrapy.Request(url=f'https://dvdhd.me{page}', callback=self.parse)
            urls = response.xpath("//div[@class='m-movies clearfix']/article[@class='u-movie']/a/@href").extract()
            names = response.xpath("//div[@class='m-movies clearfix']/article[@class='u-movie']/a/h2/text()").extract()
            for i in range(len(urls)):
                item = BookItem()
                item['book_url'] = f'https://dvdhd.me{urls[i]}'
                item['book_name'] = names[i]
                yield item

        except Exception as e:
            print(e)
            return
