# -*- coding: utf-8 -*-
import scrapy
from zhconv import convert

from helloScrapy.items import BookItem


class VolmoeSpider(scrapy.Spider):
    name = 'volmoe'
    allowed_domains = ['volmoe.com']
    # start_urls = [f'https://volmoe.com/l/all,all,all,sortpoint,all,all/{i}.htm' for i in range(1, 2)]
    start_urls = [f'https://volmoe.com/l/all,all,all,sortpoint,all,all/{i}.htm' for i in range(1, 473)]

    # /html/body/div[8]/table/tbody/tr[2]/td[1]/a[2]/font/font

    # 自动调用 parse ，解析 item URL
    def parse(self, response):
        itemUrlList = list(set(response.xpath('/html/body/div[7]/table') \
                               .xpath('//a/@href') \
                               .re(r'https://volmoe.com/c/\d+.htm')))
        for itemUrl in itemUrlList:
            yield scrapy.Request(url=itemUrl, callback=self.parse_item)

    # 手动调用 parse_item ，解析 item
    def parse_item(self, response):
        try:
            item = BookItem()
            item['book_url'] = response.url
            item['book_name'] = convert(response.xpath('//div/b/text()').extract()[0], 'zh-cn')
            item['book_desc'] = convert(response.xpath('//*[@id="desc_text"]/text()').extract()[0].strip(), 'zh-cn')
            yield item
        except Exception as e:
            print(e)
            return
