# -*- coding: utf-8 -*-

import json

import redis
from sonic import IngestClient
from environs import Env

host = '127.0.0.1'
port = 6379
env = Env()
env.read_env()

InCrontab = env.bool("InCrontab", False)


class MoviesPipeline(object):

    def __init__(self):
        # self.file = open('movies.json', 'a', encoding='utf-8')
        self.ingestcl = IngestClient("8.136.0.121", '1491', "SecretPassword")
        self.r = redis.StrictRedis(host=host, port=port, password='redispassword')

    def process_item(self, item, spider):
        # text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        # self.file.write(text)
        url = item['url']
        # movieUpdate 中需要用到 url, 暂时不删除了
        # del item['url']
        itemjson = json.dumps(dict(item), ensure_ascii=False)
        # 清除 sonic, 重新爬取数据
        # n = self.r.hset(name='movies', key=url, value=itemjson)
        # if n > 0:
        if True:
            self.ingestcl.push(collection="movies", bucket="default",
                               object=url, text=item['name'],
                               lang=None)
            # 如果是定时爬取, 在资源更新后, 加入特定队列中
            if InCrontab:
                self.r.rpush('movieUpdate', itemjson)
        # 会将item打印到屏幕上，方便观察
        return item

    def close_spider(self, spider):
        # self.file.close()
        self.r.close()
        self.ingestcl.close()
