# -*- coding: utf-8 -*-

import json

import redis
from sonic import IngestClient

host = '127.0.0.1'
port = 6379


class MoviesPipeline(object):

    def __init__(self):
        # self.file = open('movies.json', 'a', encoding='utf-8')
        self.ingestcl = IngestClient("127.0.0.1", '1491', "SecretPassword")
        self.r = redis.StrictRedis(host=host, port=port)

    def process_item(self, item, spider):
        # text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        # self.file.write(text)
        n = self.r.hset(name='movies', key=item['book_url'], value=item['book_name'])
        if n > 0:
            self.ingestcl.push(collection="movies", bucket="default",
                               object=item['book_url'], text=item['book_name'],
                               lang=None)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        # self.file.close()
        self.r.close()
        self.ingestcl.close()


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
