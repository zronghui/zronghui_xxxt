# -*- coding: utf-8 -*-

import json


class MoviesPipeline(object):

    def __init__(self):
        self.file = open('movies.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class BooksPipeline(object):

    def __init__(self):
        self.file = open('books.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class CrontabMoviesPipeline(object):

    def __init__(self):
        self.file = open('CrontabMovies.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()


class CrontabBooksPipeline(object):

    def __init__(self):
        self.file = open('CrontabBooks.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(text)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        self.file.close()
