# -*- coding: utf-8 -*-
import scrapy

from helloScrapy.items import BookItem


class AxcsSpider(scrapy.Spider):
    name = 'axcs'
    allowed_domains = ['www.zxcs.me']
    start_urls = '''http://www.zxcs.me/sort/23
http://www.zxcs.me/sort/25
http://www.zxcs.me/sort/26
http://www.zxcs.me/sort/27
http://www.zxcs.me/sort/28
http://www.zxcs.me/sort/29
http://www.zxcs.me/sort/55
http://www.zxcs.me/sort/36
http://www.zxcs.me/sort/37
http://www.zxcs.me/sort/38
http://www.zxcs.me/sort/39
http://www.zxcs.me/sort/40
http://www.zxcs.me/sort/41
http://www.zxcs.me/sort/42
http://www.zxcs.me/sort/43
http://www.zxcs.me/sort/44
http://www.zxcs.me/sort/45
'''.split()

    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
        'ITEM_PIPELINES': {'helloScrapy.pipelines.AxcsPipeline': 300},
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'
        },
    }

    def parse(self, response):
        try:
            pages = response.xpath("//div[@id='pagenavi']/a/@href").extract()
            for page in pages:
                yield scrapy.Request(url=page, callback=self.parse)
            urls = response.xpath("//dl[@id='plist']/dt/a/@href").extract()
            names = response.xpath("//dl[@id='plist']/dt/a/text()").extract()
            for i in range(len(urls)):
                item = BookItem()
                item['book_url'] = urls[i]
                item['book_name'] = names[i]
                yield item

        except Exception as e:
            print(e)
            return
