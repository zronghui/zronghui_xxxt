# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from helloScrapy.items import BookItem


class DoubanSpider(CrawlSpider):
    name = "douban"
    allowed_domains = ["douban.com"]
    custom_settings = {
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
        'CONCURRENT_REQUESTS_PER_IP': 100,
        'DOWNLOAD_DELAY': 1,
        'ITEM_PIPELINES': {'helloScrapy.pipelines.DoubanPipeline': 300},
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        },
    }
    # start_urls = ['https://book.douban.com/subject/34894380']

    start_urls = ['https://book.douban.com/tag/']
    rules = (Rule(LinkExtractor(allow=r"/tag/"), follow=True),
             Rule(LinkExtractor(allow=r"https://book\.douban\.com/subject/\d+",
                                deny=r'https://book\.douban\.com/subject/\d+/buylinks'), callback="douban_parse"))

    def douban_parse(self, response):
        item = BookItem()
        item['book_url'] = response.url
        item['book_name'] = response.xpath("//h1/span/text()").extract_first()
        item['book_author'] = response.css('#info a::text').extract_first()
        book_score = response.xpath("//strong[@class='ll rating_num ']/text()").extract_first()
        if book_score:
            item['book_score'] = book_score.strip()
        # item['book_desc'] = '\n'.join(response.css('#link-report p::text').extract())
        item['book_image'] = response.css('#mainpic img::attr(src)').extract_first()
        return item
