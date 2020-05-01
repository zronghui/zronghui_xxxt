# -*- coding: utf-8 -*-
import random

import scrapy
from environs import Env
from helloScrapy.items import BookItem
from icecream import ic

env = Env()
env.read_env()

InCrontab = env.bool("InCrontab", False)


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['movies']
    if InCrontab:
        pipeline = 'helloScrapy.pipelines.CrontabMoviesPipeline'
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
            'https://www.meijumi.net/usa/page/1',
            'https://www.meijutt.tv/1_______.html',
            *[f'https://www.wanmeikk.me/category/{i}.html' for i in range(1, 5)],
            *[f'https://www.tcmove.com/list/{i}.html' for i in ["dianying", 'lianxuju', 'zongyi', 'dongman']],
            *[f'http://www.yhdm.tv/{i}' for i in ('japan', 'china', 'american', 'movie')],
            *[f'http://www.zzzfun.com/vod-type-id-{i}-page-1.html' for i in (1, 3)],
            *[f'http://www.qimiqimi.co/type/{i}/page/1.html' for i in ('xinfan', 'riman', 'guoman', 'guoman', 'jcdm')],
            'http://www.yxdm.me/resource/15-1.html',
            *[f'https://kkmovie.cf/index.php/vod/type/id/{i}/page/1.html' for i in range(1, 5)],
            'https://miao101.com/page/1',
            *[f'https://www.kpkuang.com/vodshow/{i}-------------.html' for i in range(1, 5)],
            'http://agefans.org/catalog?page=1',
        ]
    else:
        pipeline = 'helloScrapy.pipelines.MoviesPipeline'
        start_urls = [
            # *[f'http://agefans.org/catalog?page={i}' for i in range(136 + 1)],
            # *[f'https://www.kpkuang.com/vodshow/1--------{i}-----.html' for i in range(1, 2581 + 1)],
            # *[f'https://www.kpkuang.com/vodshow/2--------{i}-----.html' for i in range(1, 618 + 1)],
            # *[f'https://www.kpkuang.com/vodshow/3--------{i}-----.html' for i in range(1, 155 + 1)],
            # *[f'https://www.kpkuang.com/vodshow/4--------{i}-----.html' for i in range(1, 316 + 1)],
            # *[f'https://miao101.com/page/{i}' for i in range(1, 2290 + 1)],
            # *[f'https://kkmovie.cf/index.php/vod/type/id/1/page/{i}.html' for i in range(1, 3947 + 1)],
            # *[f'https://kkmovie.cf/index.php/vod/type/id/2/page/{i}.html' for i in range(1, 1826 + 1)],
            # *[f'https://kkmovie.cf/index.php/vod/type/id/3/page/{i}.html' for i in range(1, 320 + 1)],
            # *[f'https://kkmovie.cf/index.php/vod/type/id/4/page/{i}.html' for i in range(1, 853 + 1)],
            # *[f'http://www.zzzfun.com/vod-type-id-1-page-{i}.html' for i in range(1, 61 + 1)],
            # *[f'http://www.zzzfun.com/vod-type-id-3-page-{i}.html' for i in range(1, 12 + 1)],
            # *[f'http://www.qimiqimi.co/type/xinfan/page/{i}.html' for i in range(1, 6 + 1)],
            # *[f'http://www.qimiqimi.co/type/riman/page/{i}.html' for i in range(1, 28 + 1)],
            # *[f'http://www.qimiqimi.co/type/guoman/page/{i}.html' for i in range(1, 6 + 1)],
            # *[f'http://www.qimiqimi.co/type/jcdm/page/{i}.html' for i in range(1, 8 + 1)],
            # *[f'http://www.yxdm.me/resource/15-{i}.html' for i in range(1, 129 + 1)],
            # *[f'http://www.yhdm.tv/japan/{i}.html' for i in range(2, 105 + 1)],
            # *[f'http://www.yhdm.tv/china/{i}.html' for i in range(2, 21 + 1)],
            # *[f'http://www.yhdm.tv/american/{i}.html' for i in range(2, 7 + 1)],
            # *[f'http://www.yhdm.tv/movie/{i}.html' for i in range(2, 12 + 1)],
            # *[f'https://www.tcmove.com/list/dianying-{i}.html' for i in range(1, 592)],
            # *[f'https://www.tcmove.com/list/lianxuju-{i}.html' for i in range(1, 193)],
            # *[f'https://www.tcmove.com/list/zongyi-{i}.html' for i in range(1, 158)],
            # *[f'https://www.tcmove.com/show/dongman--------{i}---.html' for i in range(1, 198)],
            # *[f'https://www.meijumi.net/usa/page/{i}/' for i in range(1, 218)],
            # *[f'https://www.meijutt.tv/{i}_______.html' for i in range(1, 326)],
            # *[f'https://www.wanmeikk.me/category/1-{i}.html' for i in range(1, 26)],
            # *[f'https://www.wanmeikk.me/category/2-{i}.html' for i in range(1, 8)],
            # *[f'https://www.wanmeikk.me/category/3-{i}.html' for i in range(1, 3)],
            # *[f'https://www.wanmeikk.me/category/4-{i}.html' for i in range(1, 3)],
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
        'www.meijumi.net': {
            'urlsXpath': "//h2[@class='entry-title']/a/@href",
            'namesXpath': "//h2[@class='entry-title']/a/text()"
        },
        'www.meijutt.tv': {
            'urlsXpath': "//a[@class='B font_14']/@href",
            'namesXpath': "//a[@class='B font_14']/text()"
        },
        'www.wanmeikk.me': {
            'urlsXpath': "//h4[@class='title text-overflow']/a/@href",
            'namesXpath': "//h4[@class='title text-overflow']/a/text()"
        },
        'www.tcmove.com': {
            'urlsXpath': "//a[@class='fed-list-title fed-font-xiv fed-text-center "
                         "fed-text-sm-left fed-visible fed-part-eone']/@href",
            'namesXpath': "//a[@class='fed-list-title fed-font-xiv fed-text-center "
                          "fed-text-sm-left fed-visible fed-part-eone']/text()"
        },
        'www.yhdm.tv': {
            'urlsXpath': "//ul/li/h2/a/@href | //p[@class='tname']/a/@href",
            'namesXpath': "//ul/li/h2/a/text() | //p[@class='tname']/a/text()"
        },
        'www.zzzfun.com': {
            'urlsXpath': "//ul[@class='search-result']/a/@href",
            'namesXpath': "//ul/a//div[@class='title-big']/text()"
        },
        'www.qimiqimi.co': {
            'urlsXpath': "//ul[@class='img-list']/li/a/@href",
            'namesXpath': "//ul[@class='img-list']/li/a/h2/text()"
        },
        'www.yxdm.me': {
            'urlsXpath': "//ul/li/p[1]//a/@href",
            'namesXpath': "//ul/li/p[1]//text()"
        },
        'kkmovie.cf': {
            'urlsXpath': "//div[@class='stui-pannel__bd clearfix']/ul/li//h4/a/@href",
            'namesXpath': "//div[@class='stui-pannel__bd clearfix']/ul/li//h4/a/text()"
        },
        'miao101.com': {
            'urlsXpath': "//p/a/@href",
            'namesXpath': "//p/a/text()"
        },
        'www.kpkuang.com': {
            'urlsXpath': "//ul[@class='fed-list-info fed-part-rows']/li/a/@href",
            'namesXpath': "//ul[@class='fed-list-info fed-part-rows']/li/a/text()"
        },
        'agefans.org': {
            'urlsXpath': '//*[@id="catalog_list"]/ul/li/div/div[2]/div/a/@href',
            'namesXpath': "//ul/li//a[@class='stretched-link-']/h5/text()"
        },
        # '': {
        #     'urlsXpath': "/@href",
        #     'namesXpath': "/text()"
        # },
    }

    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
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
        ic(len(urls) == len(names))
        ic(urls[0])
        ic(names[0])
        if len(urls) > 0 and urls[0].startswith('/'):
            urls = [httpDomain + i for i in urls]
        for url, name in zip(urls, names):
            item = BookItem()
            item['book_url'] = url
            item['book_name'] = name
            yield item
