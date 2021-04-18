# -*- coding: utf-8 -*-
import random

import scrapy
from environs import Env
from helloScrapy.items import MovieItem
from icecream import ic
import datetime
import random

env = Env()
env.read_env()

InCrontab = env.bool("InCrontab", False)
InTest = env.bool("InTest", False)


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['movies']
    pipeline = 'helloScrapy.pipelines.MoviesPipeline'
    if InTest:
        start_urls = [
            # www.ak1080.com Connection to the other side was lost in a non-clean fashion: Connection lost
            # https://www.wanmeikk.me/category/9.htm urls: [], names: []
            # https://www.zhenbuka.com/vodtype/1-1.html
            # https://yanetflix.com//index.php/vod/show/by/time/id/3/page/1.html
            # KeyError: 'www.yxdm.org'
            *[f'https://nfstar.net/vodshow/{i}--time------1---/' for i in (20, 21, 22, 23)],
        ]
    elif InCrontab:
        start_urls = [
            # 4k
            *[f'https://4kya.com/index.php/vod/show/by/time/id/{i}/page/1.html' for i in (1, 2, 3, 4)],
            # 超清
            # 'https://www.mdoutv.com/movie_bt/page/1',
            # 按照分类来，这样每一页要不全都有更新情况，要不全部没有，不会出现 len(desc)!=len(urls) 的情况
            *[f'https://www.mdoutv.com/movie_bt_series/{i}' for i in
              ['en', 'guocanju', 'gangtai', 'hanju', 'riju', 'movie', 'ac']],
            *[f'https://www.wanmeikk.me/category/{i}.html' for i in range(1, 11)],
            *[f'https://www.jpysvip.net/vodtype/{i}-1.html' for i in range(1, 5)],
            *[f'https://gudanys.com/vodtype/{i}-1.html' for i in range(1, 5)],
            *[f'https://www.zhenbuka.com/vodtype/{i}-1.html' for i in range(1, 5)],
            # *[f'https://www.mengmiandaxia.com/cate/{i}?sort=4' for i in range(1, 5)], # 网站去除了 web 端
            *[f'http://www.fenggoudy1.com/list-select-id-{i}-type--area--year--star--state--order-addtime.html'
              for i in range(1, 5)],
            *[f'https://www.ak1080.com/vodtype/{i}-1.html' for i in (1, 2, 3, 4)],
            *[f'https://nfstar.net/vodshow/{i}--time------1---/' for i in (20, 21, 22, 23)],
            # 美剧
            # 'https://www.meijumi.net/usa/page/1',
            'https://www.meijutt.tv/1_______.html',

            # 动漫
            # 'http://agefans.org/catalog?page=1',
            'https://www.agefans.net/update?page=1',
            *[f'http://www.bimiacg.com/type/{i}/' for i in ['juchang', 'fanzu', 'guoman', 'riman']],
            *[f'http://www.dmdm2020.com/dongmantype/{i}.html' for i in [20, 21]],
            *[f'http://www.yhdm.io/{i}' for i in ('japan', 'china', 'american', 'movie')],
            'http://www.yxdm.me/resource/15-1.html',
            *[f'http://www.zzzfun.com/vod-type-id-{i}-page-1.html' for i in (1, 3, 42)],
            *[f'https://www.qiqidongman.com/vod-search-order-vod_addtime-area-{i}-p-1.html' for i in ('%E6%97%A5%E6%9C%AC', '%E5%9B%BD%E4%BA%A7')],
            # *[f'http://www.qimiqimi.co/type/{i}/page/1.html' for i in ('xinfan', 'riman', 'guoman', 'guoman', 'jcdm')],
            'https://www.xskdm.com/vodshow/1--------1---.html', 
            'https://www.xskdm.com/vodtype/2-1.html', 
            'https://www.xskdm.com/vodtype/3-1.html',

            # 剧情、播放平台等
            'https://www.juqingba.cn/dianshiju/list_25_1.html',
            'http://www.yue365.com/tv/neidi/',
        ]
    else:
        start_urls = [
            # 2020 03 03
            # 奈飞星影视
            # [最新电影 - 推荐电影 - 奈飞星影视](https://nfstar.net/vodshow/20--time------119---/)
            # [最新美剧 - 推荐美剧 - 奈飞星影视](https://nfstar.net/vodshow/21--time------79---/)
            # [最新国语 - 推荐国语 - 奈飞星影视](https://nfstar.net/vodshow/22--time------16---/)
            # [最新日韩 - 推荐日韩 - 奈飞星影视](https://nfstar.net/vodshow/23--time------15---/)
            *[f'https://nfstar.net/vodshow/{_type}--time------{i}---/'
              for _type, n in [(20, 40), (21, 30), (22, 16), (23, 15)]
              for i in range(n + 1)],
        ]
    random.shuffle(start_urls)
    ic(start_urls)

    xpath = {
        # '': {
        #     'urlsXpath': "/@href",
        #     'namesXpath': "/text()"
        # },
        # 4k
        '4kya.com': {
            'urlsXpath': "//ul/li//h4[@class='title text-overflow']/a/@href",
            'namesXpath': "//ul/li//h4[@class='title text-overflow']/a/text()",
            'imgXpath': "//ul/li/div/a/@data-original",
            'descXpath': "//ul/li//span[@class='pic-text text-right']/text()",
        },
        # 超清
        'www.mengmiandaxia.com': {
            'urlsXpath': "//ul/li//h4[@class='title text-overflow']/a/@href",
            'namesXpath': "//ul/li//h4[@class='title text-overflow']/a/text()",
            'imgXpath': "//img[@class='cover-image']/@src",
            'descXpath': "//ul/li//span[@class='pic-text text-right']/text()",
        },
        'www.fenggoudy1.com': {
            'urlsXpath': "//ul/li//span[@class='s_tit']/a/@href",
            'namesXpath': "//ul/li//span[@class='s_tit']/a/text()",
            'imgXpath': "//ul/li//div[@class='v_pic']/img/@src",
            'descXpath': "//ul/li//div[@class='v_pic']/span//text()",
        },
        'www.mdoutv.com': {
            'urlsXpath': "//h3/a/@href",
            'namesXpath': "//h3/a/text()",
            'imgXpath': "//ul/li/a/img/@data-original",
            'descXpath': "//ul/li/a/div/span/text()",
        },
        'www.wanmeikk.me': {
            'urlsXpath': "//h4[@class='title text-overflow']/a/@href",
            'namesXpath': "//h4[@class='title text-overflow']/a/text()",
            'imgXpath': "//ul/li/div/a/@data-original",
            'descXpath': "//ul/li/div/a/span[2]/text()",
        },
        'www.ak1080.com': {
            'urlsXpath': "//ul/li//h4[@class='title text-overflow']/a/@href",
            'namesXpath': "//ul/li//h4[@class='title text-overflow']/a/text()",
            'imgXpath': "//ul/li/div/a/@data-original",
            'descXpath': "//ul/li//span[@class='pic-text text-left']/text()",
        },
        'nfstar.net': {
            'urlsXpath': "//ul/li//h4[@class='title text-overflow']/a/@href",
            'namesXpath': "//ul/li//h4[@class='title text-overflow']/a/text()",
            'imgXpath': "//ul/li/div/a/@data-original",
            'descXpath': "//ul/li//span[@class='pic-text text-left']/text()",
        },
        # 下面这三个网站格式都一样
        'www.jpysvip.net': {
            'urlsXpath': "//ul/li//h4[@class='title text-overflow']/a/@href",
            'namesXpath': "//ul/li//h4[@class='title text-overflow']/a/text()",
            'imgXpath': "//ul/li/div/a/@data-original",
            'descXpath': "//ul/li//span[@class='pic-text text-right']/text()",
        },
        'gudanys.com': {
            'urlsXpath': "//ul/li//h4[@class='title text-overflow']/a/@href",
            'namesXpath': "//ul/li//h4[@class='title text-overflow']/a/text()",
            'imgXpath': "//ul/li/div/a/@data-original",
            'descXpath': "//ul/li//span[@class='pic-text text-right']/text()",
        },
        'www.zhenbuka.com': {
            'urlsXpath': "//h4[@class='title text-overflow']/a/@href",
            'namesXpath': "//h4[@class='title text-overflow']/a/text()",
            'imgXpath': "//ul/li/div/a/@data-original",
            'descXpath': "//ul/li//span[@class='pic-text text-right']/text()",
        },
        # 美剧
        # 'www.meijumi.net': {
        #     'urlsXpath': "//h2[@class='entry-title']/a/@href",
        #     'namesXpath': "//h2[@class='entry-title']/a/text()",
        #     'imgXpath': "/@data-original",
        #     'descXpath': "/text()",
        # },
        'www.meijutt.tv': {
            'urlsXpath': "//a[@class='B font_14']/@href",
            'namesXpath': "//a[@class='B font_14']/text()",
            'imgXpath': "//div[@class='bor_img3_right']/a/img[@class='list_pic']/@src",
            'descXpath': "//ul[@class='list_20']/li/span/font/text()",
        },
        # 动漫
        'agefans.org': {
            'urlsXpath': '//*[@id="catalog_list"]/ul/li/div/div[2]/div/a/@href',
            'namesXpath': "//ul/li//a[@class='stretched-link-']/h5/text()",
            'imgXpath': "//li/div//img[@class='card-img- ']/@src",
            # 'descXpath': "/text()",
        },
        'www.bimiacg.com': {
            'urlsXpath': "//ul/li/div[@class='info']/a/@href",
            'namesXpath': "//ul/li/div[@class='info']/a/text()",
            'imgXpath': "//ul/li/a[@class='img']/img/@data-original",
            'descXpath': "//ul/li/div[@class='info']/p/span[@class='fl']/text()",
        },
        'www.dmdm2020.com': {
            'urlsXpath': "//ul/li//h4/a/@href",
            'namesXpath': "//ul/li//h4/a/text()",
            'imgXpath': "//ul/li/div/a/@data-original",
            'descXpath': "//ul/li//span[@class='pic-text text-right']/text()",
        },
        'www.yhdm.io': {
            'urlsXpath': "//ul/li/h2/a/@href | //p[@class='tname']/a/@href",
            'namesXpath': "//ul/li/h2/a/text() | //p[@class='tname']/a/text()",
            'imgXpath': "//ul/li/a/img/@src",
            'descXpath': "//ul/li/span[1]/font/text()",
        },
        'www.yxdm.me': {
            'urlsXpath': "//ul/li/p[1]//a/@href",
            'namesXpath': "//ul/li/p[1]//text()",
            'imgXpath': "//ul/li/p[1]/a/img/@src",
            'descXpath': "//ul/li/p[4]//text()",
        },
        'www.agefans.net': {
            'urlsXpath': '//ul/li/h4/a/@href',
            'namesXpath': "//ul/li/h4/a/text()",
            'imgXpath': "//ul/li/a/img/@src",
            'descXpath': "//ul/li/a/span/text()",
        },
        'www.zzzfun.com': {
            'urlsXpath': "//ul[@class='search-result']/a/@href",
            'namesXpath': "//ul/a//div[@class='title-big']/text()",
            'imgXpath': "//ul/a/div[@class='d-cover-big']/img/@src",
            'descXpath': "//ul/a/div[@class='d-text-big']/div[@class='title-sub']/span[1]/text()",
        },
        'www.qiqidongman.com': {
            'urlsXpath': "//ul/li/a[@class='img']/@href",
            'namesXpath': "//ul/li/a[@class='img']/i[@class='tit']/text()",
            'imgXpath': "//ul/li/a[@class='img']/img/@src",
            'descXpath': "//ul/li/div[@class='info']/p[@class='date']/text()",
        },
        'www.xskdm.com': {
            'urlsXpath': "//ul/li//h4[@class='title text-overflow']/a/@href",
            'namesXpath': "//ul/li//h4[@class='title text-overflow']/a/text()",
            'imgXpath': "//ul/li/div/a/@data-original",
            'descXpath': "//ul/li//span[@class='pic-text text-right']/text()",
        },
        # 剧情、播放平台等
        'www.yue365.com': {
            'urlsXpath': "//ul/li/div[@class='mv_name']/a/@href",
            'namesXpath': "//ul/li/div[@class='mv_name']/a/text()",
            # 'imgXpath': "/@data-original",
            # 'descXpath': "/text()",
        },
        'www.juqingba.cn': {
            'urlsXpath': "//ul[@class='m_Box8 w110 FL']/li/a/@href",
            'namesXpath': "//ul[@class='m_Box8 w110 FL']/li/a/img/@alt",
            'imgXpath': "//ul/li/div[@class='a_img']/a/img/@src",
            # 'descXpath': "/text()",
        },
        # 其他
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
        'app.movie': {
            'urlsXpath': "//h4[@class='stui-vodlist__title']/a/@href",
            'namesXpath': "//h4[@class='stui-vodlist__title']/a/text()"
        },
        'www.tcmove.com': {
            'urlsXpath': "//a[@class='fed-list-title fed-font-xiv fed-text-center "
                         "fed-text-sm-left fed-visible fed-part-eone']/@href",
            'namesXpath': "//a[@class='fed-list-title fed-font-xiv fed-text-center "
                          "fed-text-sm-left fed-visible fed-part-eone']/text()"
        },
        'www.qimiqimi.co': {
            'urlsXpath': "//ul[@class='img-list']/li/a/@href",
            'namesXpath': "//ul[@class='img-list']/li/a/h2/text()"
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
        'www.66zhibo.net': {
            'urlsXpath': "//ul/li[@class='p-item']/a/@href",
            'namesXpath': "//ul/li[@class='p-item']/a//strong/text()"
        },
        'www.bubulai.com': {
            'urlsXpath': "//ul/li/dl/p[1]/a/@href",
            'namesXpath': "//ul/li/dl/p[1]/a/text()"
        },
        'www.novipnoad.com': {
            'urlsXpath': "//div[@class='col-md-3 col-sm-6 col-xs-6 ']//h3/a/@href",
            'namesXpath': "//div[@class='col-md-3 col-sm-6 col-xs-6 ']//h3/a/text()"
        },
    }

    custom_settings = {
        # 'LOG_LEVEL': "WARNING",
        'CONCURRENT_REQUESTS': 5,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'CONCURRENT_REQUESTS_PER_IP': 2,
        'DOWNLOAD_DELAY': 1,
        'DOWNLOAD_TIMEOUT': 20,
        'ITEM_PIPELINES': {pipeline: 300},
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36',
        },
    }

    def parse(self, response):
        domain = response.url.split('/', 3)[2]
        httpDomain = '/'.join(response.url.split('/', 3)[:3])
        now = datetime.datetime.now().isoformat()
        ic(now)
        ic(response.url)
        urls = response.xpath(self.xpath[domain]["urlsXpath"]).extract()
        names = response.xpath(self.xpath[domain]["namesXpath"]).extract()
        if not urls or len(urls) != len(names):
            ic(urls, names)
            return

        imgs = ['' for _ in range(len(urls))]
        descs = ['' for _ in range(len(urls))]
        if 'imgXpath' in self.xpath[domain] and self.xpath[domain]["imgXpath"]:
            t = response.xpath(self.xpath[domain]["imgXpath"]).extract()
            if len(t) == len(urls):
                imgs = t
        if 'descXpath' in self.xpath[domain] and self.xpath[domain]["descXpath"]:
            t = response.xpath(self.xpath[domain]["descXpath"]).extract()
            if len(t) == len(urls):
                descs = t
        
        descs = list(i.strip() for i in descs)
        complete(urls, httpDomain)
        complete(imgs, httpDomain)
        ic(len(names), urls[0], names[0], imgs[0], descs[0])
        print()
        for i in range(len(urls)):
            item = MovieItem()
            item['url'] = urls[i]
            item['name'] = names[i]
            if imgs[i]:
                item['img'] = imgs[i]
            if descs[i]:
                item['desc'] = descs[i]
            yield item


def complete(urls, httpDomain):
    for i in range(len(urls)):
        if urls[i].startswith('/'):
            urls[i] = httpDomain + urls[i]
