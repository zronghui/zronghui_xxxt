# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class HelloscrapyPipeline(object):

    def __init__(self):
        self.file = open('books.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class DoubanPipeline(object):

    def __init__(self):
        self.file = open('douban.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class ShudanPipeline(object):

    def __init__(self):
        self.file = open('shudan.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class XiangZhanPipeline(object):

    def __init__(self):
        self.file = open('xiangzhan.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class AxcsPipeline(object):

    def __init__(self):
        self.file = open('axcs.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class Java1234Pipeline(object):

    def __init__(self):
        self.file = open('java1234.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class DvdhdPipeline(object):

    def __init__(self):
        self.file = open('dvdhd.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class ItsckPipeline(object):

    def __init__(self):
        self.file = open('itsck.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class ZhenbukaPipeline(object):

    def __init__(self):
        self.file = open('zhenbuka.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class BttwoPipeline(object):

    def __init__(self):
        self.file = open('bttwo.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class DdrkPipeline(object):

    def __init__(self):
        self.file = open('ddrk.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class PiankuPipeline(object):

    def __init__(self):
        self.file = open('pianku.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()
