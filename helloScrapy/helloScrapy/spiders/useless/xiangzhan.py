# -*- coding: utf-8 -*-
import scrapy

from helloScrapy.items import BookItem


class XiangzhanSpider(scrapy.Spider):
    name = 'xiangzhan'
    allowed_domains = ['slfswh.xiangzhan.com/']
    start_urls = [f'http://slfswh.xiangzhan.com/p-article_detail/id-{i}.html'
                  for i in range(1, 900)]
    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
        'ITEM_PIPELINES': {'helloScrapy.pipelines.XiangZhanPipeline': 300},
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'
        },
    }

    def parse(self, response):
        try:
            item = BookItem()
            item['book_url'] = response.url
            item['book_name'] = response.xpath("//h3[@class='article_detail_title article_detail_5_title bf ic']/text()") \
                .extract_first()
            yield item
        except Exception as e:
            print(e)
            return
