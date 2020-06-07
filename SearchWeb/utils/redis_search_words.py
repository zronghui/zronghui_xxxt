#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pretty_errors
import redis

pretty_errors.activate()

host = '127.0.0.1'
port = 6379
r = redis.StrictRedis(host=host, port=port)


def get_hot_search_words():
    q = r.zrangebyscore(name='search_rank', min=0, max=100, withscores=True)
    return [{'word': i[0].decode("utf-8"), 'hot': i[1]} for i in reversed(q)][:10]


def search(w):
    r.zincrby(name='search_rank', amount=1, value=w)
