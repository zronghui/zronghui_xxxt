# -*- coding: utf-8 -*-
import random

import scrapy
from icecream import ic

from helloScrapy.items import BookItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['movies']
    start_urls = [
        'https://www.bttwo.com/new-movie/page/1',
        'https://ddrk.me/page/1',
        *[f'https://dvdhd.me/list/index{i}.html' for i in range(1, 6)],
        *[f'https://www.itsck.com/type/{i}.html' for i in
          ['dianying', 'lianxuju', 'zongyi', 'dongman']
          ],
        *[f'https://www.zhenbuka.com/vodtype/{i}' for i in range(1, 5)],
        *[f'https://app.movie/index.php/vod/type/id/{i}/page/1.html' for i in range(1, 5)],
        *[f'https://app.movie/index.php/vod/type/id/1/page/{i}.html' for i in random.sample(range(2, 1298), 6)],
        *[f'https://app.movie/index.php/vod/type/id/2/page/{i}.html' for i in random.sample(range(2, 562), 3)],
        *[f'https://app.movie/index.php/vod/type/id/3/page/{i}.html' for i in random.sample(range(2, 119), 1)],
        *[f'https://app.movie/index.php/vod/type/id/4/page/{i}.html' for i in random.sample(range(2, 229), 1)],
    ]
    ic(start_urls)

    xpath = {
        'www.bttwo.com': {
            'urlsXpath': "//h3[@class='dytit']/a/@href",
            'namesXpath': "//h3[@class='dytit']/a/text()"
        },
        'ddrk.me': {
            'urlsXpath': "//h2[@class='post-box-title']/a/@href",
            'namesXpath': "//h2[@class='post-box-title']/a/text()"
        },
        'dvdhd.me': {
            'urlsXpath': "//div[@class='m-movies clearfix']/article[@class='u-movie']/a/@href",
            'namesXpath': "//div[@class='m-movies clearfix']/article[@class='u-movie']/a/h2/text()"
        },
        'www.itsck.com': {
            'urlsXpath': "//a[@class='fed-list-title fed-font-xiv fed-text-center "
                         "fed-text-sm-left fed-visible fed-part-eone']/@href",
            'namesXpath': "//a[@class='fed-list-title fed-font-xiv fed-text-center "
                          "fed-text-sm-left fed-visible fed-part-eone']/text()"
        },
        'www.zhenbuka.com': {
            'urlsXpath': "//h4[@class='title text-overflow']/a/@href",
            'namesXpath': "//h4[@class='title text-overflow']/a/text()"
        },
        'app.movie': {
            'urlsXpath': "//h4[@class='stui-vodlist__title']/a/@href",
            'namesXpath': "//h4[@class='stui-vodlist__title']/a/text()"
        },
    }

    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
        'ITEM_PIPELINES': {'helloScrapy.pipelines.MoviesPipeline': 300},
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
