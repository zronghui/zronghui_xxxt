# -*- coding: utf-8 -*-
import os
from os.path import exists, join

import scrapy
import wget


class GqzzwSpider(scrapy.Spider):
    name = 'gqzzw'
    allowed_domains = ['gqzzw.com']

    custom_settings = {
        'CONCURRENT_REQUESTS': 3,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 3,
        'CONCURRENT_REQUESTS_PER_IP': 3,
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
    }

    def __init__(self, lastPage=None, zzname=None, name=None, **kwargs):
        super().__init__(name=None, **kwargs)

        print(lastPage, zzname)
        self.pgNum = lastPage.split('/')[-1]
        self.zztype = lastPage.split('/')[-2]
        self.zzName = zzname

        self.start_urls = [f'http://www.gqzzw.com/type/{self.zztype}/{i}' for i in range(1, int(self.pgNum) + 1)]

        self.outdir = '/Volumes/My Passport/data/ut下载/77     书籍/杂志/' + self.zzName
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir, exist_ok=True)

    def parse(self, response):
        itemUrlList = response.xpath('//li[@class="row center-block book"]/a/@href').extract()
        for itemUrl in itemUrlList:
            yield scrapy.Request(url='http://www.gqzzw.com' + itemUrl, callback=self.parse_item)

    # 手动调用 parse_item ，解析 item
    def parse_item(self, response):
        l = response.xpath("//div[@class='col-md-9']/div[@class=' books'][1]/node()").extract()
        for i in l:
            if i.startswith('<!--<a href='):
                print(i)
                book_url = i.split(' ')[1][6:-1]
                book_name = book_url.split('?')[0].rsplit('/', 1)[1]
                if exists(join(self.outdir, book_name)):
                    print('已存在', join(self.outdir, book_name))
                    continue
                print(book_url)
                wget.download(book_url, out=self.outdir, bar=wget.bar_thermometer)
