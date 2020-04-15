# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    book_url = scrapy.Field()
    book_desc = scrapy.Field()
    book_score = scrapy.Field()
    book_author = scrapy.Field()
    book_image = scrapy.Field()

    book_type = scrapy.Field()
    book_format = scrapy.Field()
    book_time = scrapy.Field()
    book_size = scrapy.Field()
    book_downl_url = scrapy.Field()
    book_source = scrapy.Field()
    book_intro = scrapy.Field()
