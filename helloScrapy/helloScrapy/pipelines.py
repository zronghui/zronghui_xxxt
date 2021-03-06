# -*- coding: utf-8 -*-

import json

import redis
from sonic import IngestClient
from environs import Env
from icecream import ic

host = '127.0.0.1'
port = 6379
env = Env()
env.read_env()

InCrontab = env.bool("InCrontab", False)


class MoviesPipeline(object):

    def __init__(self):
        # self.file = open('movies.json', 'a', encoding='utf-8')
        self.ingestcl = IngestClient("8.136.0.121", '1491', "SecretPassword")
        self.r = redis.StrictRedis(host=host, port=port, password='redispassword',
                                   decode_responses=True, charset='utf-8')

    def isupdate(self, key, item):
        if not self.r.hexists(name='movies', key=key):
            return True
        if not item.get('desc', ''):
            return False
        oldValue = self.r.hget(name='movies', key=key)
        if not oldValue.startswith('{'):
            return True
        d = json.loads(oldValue)
        return item.get('desc', '') == d.get('desc', '')

    def process_item(self, item, spider):
        # text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        # self.file.write(text)
        url = item['url']
        # movieUpdate 中需要用到 url, 暂时不删除了
        # del item['url']
        itemjson = json.dumps(dict(item), ensure_ascii=False)
        # 如果是定时爬取, 在资源更新后, 加入特定队列中
        if InCrontab and self.isupdate(key=url, item=item):
            self.r.rpush('movieUpdate', itemjson)
        n = self.r.hset(name='movies', key=url, value=itemjson)
        # n = 1 表示新的 Field 被设置了新值，0 表示 Field 已经存在，用新值覆盖原有值, 但是不表示没有更新
        # 放在外面, 确保 sonic 中有最新的数据
        self.ingestcl.push(collection="movies", bucket="default",
                           object=url, text=item['name'],
                           lang=None)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        # self.file.close()
        self.r.close()
        self.ingestcl.close()
