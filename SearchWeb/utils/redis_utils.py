#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import pretty_errors
import redis
from environs import Env

pretty_errors.activate()

env = Env()
env.read_env()

host = '127.0.0.1'
port = 6379
if not env.str('redispassword', ''):
    print('请在终端设置 Redis 密码')
    sys.exit(-1)
r = redis.StrictRedis(host=host, port=port, password=env.str('redispassword', ''))


# def get_hot_search_words():
#     q = r.zrangebyscore(name='search_rank', min=0, max=100, withscores=True)
#     return [{'word': i[0].decode("utf-8")[:10], 'hot': i[1]} for i in reversed(q)][:10]
#
#
# def search(w):
#     r.zincrby(name='search_rank', amount=1, value=w)
def getMoviesByUrls(urls):
    n = len(urls)
    res = [{} for _ in range(n)]
    names = [name.decode("utf-8") for name in r.hmget('movies', urls)]
    for i in range(n):
        res[i]['book_url'] = urls[i]
        res[i]['book_name'] = names[i]
    return res
