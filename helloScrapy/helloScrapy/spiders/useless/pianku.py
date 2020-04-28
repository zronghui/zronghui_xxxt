# -*- coding: utf-8 -*-
import scrapy

from helloScrapy.items import BookItem


class PiankuSpider(scrapy.Spider):
    name = 'pianku'
    allowed_domains = ['www.pianku.tv']
    start_urls = [f'http://www.pianku.tv/{i}' for i in ['mv', 'tv', 'ac']]

    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
        'ITEM_PIPELINES': {'helloScrapy.pipelines.PiankuPipeline': 300},
        'DEFAULT_REQUEST_HEADERS': {
            'referer': 'https://www.pianku.tv/py/lJ2ZjpWY5gGa_8.html',
            'cookie': 'Hm_lvt_5a21a69d1b034aed24dcda25771e8135=1587552999; '
                      'PHPSESSID=peraj43cs4s2sra5sm86svqhq4; '
                      'player123=%u897F%u90E8%u4E16%u754C%u7B2C%u4E09%u5B63%u'
                      '7B2C06%u96C6%23%23/py/lJmZrRzM3MTZ_6.html%23%231085%23%'
                      '2331%24%24%u6211%u662F%u4F59%u6B22%u6C34%u7B2C03%u96C6%2'
                      '3%23/py/lJ2ZkdzYqxWa_3.html%23%231536%23%2359%24%24%u592'
                      'B%u59BB%u7684%u4E16%u754C%u7B2C08%u96C6%23%23/py/lJ2ZjpW'
                      'Y5gGa_8.html%23%231451%23%2333%24%24%u4E0D%u6B7B%u4E4B%u'
                      '8EABHD%u4E2D%u5B57%23%23/py/lJ2ZoNmYplWZ_1.html%23%231272%23%2324%24%24; '
                      'Hm_lpvt_5a21a69d1b034aed24dcda25771e8135=1587561978',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'
        },
    }


def parse(self, response):
    try:
        pages = response.xpath("//div[@class='pages']/a/@href") \
            .extract()
        for page in pages:
            yield scrapy.Request(url=f'https://www.pianku.tv{page}', callback=self.parse)
        urls = response.xpath("//div[@class='li-bottom']/h3/a/@href").extract()
        names = response.xpath("//div[@class='li-bottom']/h3/a/text()").extract()
        for i in range(len(urls)):
            item = BookItem()
            item['book_url'] = f'https://www.pianku.tv{urls[i]}'
            item['book_name'] = names[i]
            yield item

    except Exception as e:
        print(e)
        return
