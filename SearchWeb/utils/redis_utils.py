#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import pretty_errors
import redis

pretty_errors.activate()

host = '127.0.0.1'
port = 6379
r = redis.StrictRedis(host=host, port=port, password='redispassword', decode_responses=True, charset='utf-8')


# def get_hot_search_words():
#     q = r.zrangebyscore(name='search_rank', min=0, max=100, withscores=True)
#     return [{'word': i[0].decode("utf-8")[:10], 'hot': i[1]} for i in reversed(q)][:10]
#
#
# def search(w):
#     r.zincrby(name='search_rank', amount=1, value=w)
def getMoviesByUrls(urls):
    if not urls: return []
    n = len(urls)
    res = [{} for _ in range(n)]
    names = [name for name in r.hmget('movies', urls)]
    for i in range(n):
        res[i]['book_url'] = urls[i]
        res[i]['book_name'] = names[i]
    return res


if __name__ == '__main__':
    res = r.hget('movies', 'https://hanmiys.com/voddetail/119280.html')
    print(res)
    res = r.hmget('movies', ['https://hanmiys.com/voddetail/119280.html', 'https://www.wanmeikk.me/project/1985.html'])
    print(res)
