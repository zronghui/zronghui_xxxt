# -*- coding: utf-8 -*-
import random

import scrapy
from environs import Env
from helloScrapy.items import MovieItem
from icecream import ic
import datetime

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
            *[f'https://www.ak1080.com/vodtype/{i}-1.html' for i in (1, 2, 3, 4)],
            *[f'https://www.qiqidongman.com/vod-search-order-vod_addtime-area-{i}-p-1.html' for i in ('%E6%97%A5%E6%9C%AC', '%E5%9B%BD%E4%BA%A7')],
            'https://www.xskdm.com/vodshow/1--------3---.html', 
            'https://www.xskdm.com/vodtype/2-2.html', 
            'https://www.xskdm.com/vodtype/3-7.html', 
        ]
    elif InCrontab:
        start_urls = [
            # 超清
            # 'https://www.mdoutv.com/movie_bt/page/1',
            # 按照分类来，这样每一页要不全都有更新情况，要不全部没有，不会出现 len(desc)!=len(urls) 的情况
            *[f'https://www.mdoutv.com/movie_bt_series/{i}' for i in
              ['en', 'guocanju', 'gangtai', 'hanju', 'riju', 'movie', 'ac']],
            *[f'https://www.wanmeikk.me/category/{i}.html' for i in range(1, 11)],
            *[f'https://www.jpysvip.net/vodtype/{i}-1.html' for i in range(1, 5)],
            *[f'https://hanmiys.com/vodtype/{i}-1.html' for i in range(1, 5)],
            *[f'https://www.zhenbuka.com/vodtype/{i}-1.html' for i in range(1, 5)],
            # *[f'https://www.mengmiandaxia.com/cate/{i}?sort=4' for i in range(1, 5)], # 网站去除了 web 端
            *[f'http://www.fenggoudy1.com/list-select-id-{i}-type--area--year--star--state--order-addtime.html'
              for i in range(1, 5)],
            *[f'https://www.ak1080.com/vodtype/{i}-1.html' for i in (1, 2, 3, 4)],
            # 美剧
            # 'https://www.meijumi.net/usa/page/1',
            'https://www.meijutt.tv/1_______.html',

            # 动漫
            # 'http://agefans.org/catalog?page=1',
            'https://www.agefans.net/update?page=1',
            *[f'http://www.bimiacg.com/type/{i}/' for i in ['juchang', 'fanzu', 'guoman', 'riman']],
            *[f'http://www.dmdm2020.com/dongmantype/{i}.html' for i in [20, 21]],
            *[f'http://www.yhdm.tv/{i}' for i in ('japan', 'china', 'american', 'movie')],
            'http://www.yxdm.me/resource/15-1.html',
            *[f'http://www.zzzfun.com/vod-type-id-{i}-page-1.html' for i in (1, 3, 42)],
            *[f'https://www.qiqidongman.com/vod-search-order-vod_addtime-area-{i}-p-1.html' for i in ('%E6%97%A5%E6%9C%AC', '%E5%9B%BD%E4%BA%A7')],
            # *[f'http://www.qimiqimi.co/type/{i}/page/1.html' for i in ('xinfan', 'riman', 'guoman', 'guoman', 'jcdm')],
            

            # 低质量
            # 'https://www.bttwo.com/new-movie/page/1',
            # 'https://ddrk.me/page/1',
            # *[f'https://www.itsck.com/type/{i}.html' for i in ['dianying', 'lianxuju', 'zongyi', 'dongman']],
            # *[f'https://www.zhenbuka.com/vodtype/{i}' for i in range(1, 5)],
            # *[f'https://www.tcmove.com/list/{i}.html' for i in ["dianying", 'lianxuju', 'zongyi', 'dongman']],
            # *[f'https://kkmovie.cf/index.php/vod/type/id/{i}/page/1.html' for i in range(1, 5)],
            # 'https://miao101.com/page/1',
            # *[f'https://www.kpkuang.com/vodshow/{i}-------------.html' for i in range(1, 5)],
            # *[f'http://www.bubulai.com/zv/{i}.html' for i in [10, 11]],
            # *[f'https://www.novipnoad.com/tv/{i}/' for i in
            #   ['hongkong', 'taiwan', 'western', 'japan', 'korea',
            #    'other', 'anime', 'shows', 'life', 'movie']],

            # 剧情、播放平台等
            'https://www.juqingba.cn/dianshiju/list_25_1.html',
            'http://www.yue365.com/tv/neidi/',
        ]
    else:
        start_urls_v1 = [
            # 超清
            # *[f'https://www.mdoutv.com/movie_bt/page/{i}' for i in range(1, 188)],
            *[f'https://www.wanmeikk.me/category/{_type}-{pageNo}.html'
              for _type, n in [(1, 30), (2, 10), (3, 3), (4, 3), (5, 12), (6, 8), (7, 1), (8, 1), (9, 1), (10, 1)]
              for pageNo in range(n + 1)],
            *[f'https://www.jpysvip.net/vodtype/{_type}-{i}.html'
              for _type, n in [(1, 676), (2, 217), (3, 30), (4, 102)]
              for i in range(n + 1)],
            *[f'https://hanmiys.com/vodtype/{_type}-{i}.html'
              for _type, n in [(1, 764), (2, 333), (3, 77), (4, 183)]
              for i in range(n + 1)],
            *[f'https://www.zhenbuka.com/vodtype/{_type}-{i}.html'
              for _type, n in [(1, 774), (2, 363), (3, 46), (4, 100)]
              for i in range(n + 1)],
            # 动漫
            *[f'http://agefans.org/catalog?page={i}' for i in range(1, 208)],
            *[f'http://www.bimiacg.com/type/{_type}-{i}/'
              for _type, n in [('juchang', 15), ('fanzu', 65), ('guoman', 6), ('riman', 6)]
              for i in range(n + 1)],
            *[f'http://www.dmdm2020.com/dongmantype/{_type}/page/{i}.html'
              for _type, n in [(20, 31), (21, 3)]
              for i in range(n + 1)],
            *[f'http://www.yhdm.io/{_type}/{i}.html'
              for _type, n in [('japan', 108), ('china', 22), ('american', 7), ('movie', 12)]
              for i in range(n + 1)],
            *[f'http://www.yxdm.me/resource/15-{i}.html' for i in range(1, 134)],
            # 美剧
            # *[f'https://www.meijumi.net/usa/page/{i}' for i in range(1, 259)],
            *[f'https://www.meijutt.tv/{i}_______.html' for i in range(1, 360)],
            # 剧情
            *[f'https://www.juqingba.cn/dianshiju/list_25_{i}.html' for i in range(1, 100)],  # omg 总共 1739页
            *[f'http://www.yue365.com/tv/neidi/index_{i}.shtml' for i in range(1, 100)],
        ]
        start_urls_v2 = [
            # 2021 02 19
            # 动漫
            *[f'https://www.agefans.net/update?page={i}' for i in range(1, 121)],
            # [ZzzFun 动漫视频网 - (￣﹃￣)~zZZ - 最新日本动漫 - 推荐日本动漫 - 第 65 页](http://www.zzzfun.com/vod_type_id_1_page_65.html)
            # [ZzzFun 动漫视频网 - (￣﹃￣)~zZZ - 最新当季新番 - 推荐当季新番 - 第 7 页](http://www.zzzfun.com/vod_type_id_42_page_7.html)
            # [ZzzFun动漫视频网 - (￣﹃￣)~zZZ-最新剧场版OVA-推荐剧场版OVA-第14页](http://www.zzzfun.com/vod_type_id_3_page_14.html)
            *[f'http://www.zzzfun.com/vod_type_id_{_type}_page_{i}.html'
              for _type, n in [(1, 65), (3, 14), (42, 7)]
              for i in range(n + 1)],
        ]
        start_urls = [
            # 2021 02 22
            # 超清
            # [1080 影视 - 超清电影 - 1080 影视 - 电影电视剧免费看](https://www.ak1080.com/vodtype/1-877.html)
            # [1080 影视 - 超清电影 - 1080 影视 - 电影电视剧免费看](https://www.ak1080.com/vodtype/2-412.html)
            # [1080 影视 - 超清电影 - 1080 影视 - 电影电视剧免费看](https://www.ak1080.com/vodtype/3-36.html)
            # [1080 影视 - 超清电影 - 1080 影视 - 电影电视剧免费看](https://www.ak1080.com/vodtype/4-109.html)
            *[f'https://www.ak1080.com/vodtype/{_type}-{i}.html'
              for _type, n in [(1, 877), (2, 412), (3, 36), (42, 109)]
              for i in range(n + 1)],
            # [【日本动漫】- 奇奇动漫 第 532 页](https://www.qiqidongman.com/vod-search-order-vod_addtime-area-%E6%97%A5%E6%9C%AC-p-532.html)
            # [【国产动漫】- 奇奇动漫 第 149 页](https://www.qiqidongman.com/vod-search-order-vod_addtime-area-%E5%9B%BD%E4%BA%A7-p-149.html)
            *[f'https://www.qiqidongman.com/vod-search-order-vod_addtime-area-{_type}-p-{i}.html'
                for _type, n in [('%E6%97%A5%E6%9C%AC', 532), ('%E5%9B%BD%E4%BA%A7', 149)]
                for i in range(n + 1)],
            # [最新连载 - 推荐连载 - 新时空动漫](https://www.xskdm.com/vodshow/1--------3---.html)
            # [最新动漫电影 - 新时空动漫](https://www.xskdm.com/vodtype/2-2.html)
            # [完结动漫 - 新时空动漫](https://www.xskdm.com/vodtype/3-7.html)
            *[f'https://www.xskdm.com/vodtype/{_type}-{i}.html'
              for _type, n in [(2, 2), (3, 7)]
              for i in range(n + 1)],
            *[f'https://www.xskdm.com/vodtype/1--------{i}---.html' for i in range(1, 3+1)],
          ]
    ic(start_urls)

    xpath = {
        # '': {
        #     'urlsXpath': "/@href",
        #     'namesXpath': "/text()"
        # },
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
        # 下面这三个网站格式都一样
        'www.jpysvip.net': {
            'urlsXpath': "//ul/li//h4[@class='title text-overflow']/a/@href",
            'namesXpath': "//ul/li//h4[@class='title text-overflow']/a/text()",
            'imgXpath': "//ul/li/div/a/@data-original",
            'descXpath': "//ul/li//span[@class='pic-text text-right']/text()",
        },
        'hanmiys.com': {
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
        'www.yhdm.tv': {
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
