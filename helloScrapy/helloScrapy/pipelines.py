# -*- coding: utf-8 -*-

import json

import redis
from sonic import IngestClient

host = '127.0.0.1'
port = 6379


class MoviesPipeline(object):

    def __init__(self):
        # self.file = open('movies.json', 'a', encoding='utf-8')
        self.ingestcl = IngestClient("101.200.240.225", '1491', "SecretPassword")
        self.r = redis.StrictRedis(host=host, port=port, password='redispassword')

    def process_item(self, item, spider):
        # text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        # self.file.write(text)
        url = item['url']
        del item['url']
        n = self.r.hset(name='movies', key=url, value=json.dumps(dict(item)))
        if n > 0:
            self.ingestcl.push(collection="movies", bucket="default",
                               object=url, text=item['name'],
                               lang=None)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        # self.file.close()
        self.r.close()
        self.ingestcl.close()
