#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import pretty_errors
import redis
import datetime

pretty_errors.activate()

host = '127.0.0.1'
port = 6379
r = redis.StrictRedis(host=host, port=port, password='redispassword', decode_responses=True, charset='utf-8')

oneDay = 24 * 60 * 60
oneMonth = oneDay * 31


def lastMonthTenDays():
    # return 上个月的 3 个十天
    # 如 ['movie-2020-11-0', 'movie-2020-11-1', 'movie-2020-11-2']
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    if month == 1:
        year -= 1
        month = 12
    else:
        month -= 1
    return [f'movie-{year}-{month}-0', f'movie-{year}-{month}-1', f'movie-{year}-{month}-2']


def lastThreeTenDays():
    # 包括当前 十天 的上 3 个十天
    # 如 ['movie-2020-11-2', 'movie-2020-12-0', 'movie-2020-12-1']
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    tenday = 0 if day < 10 else 1 if day < 20 else 2
    res = lastMonthTenDays()[tenday + 1:]
    for i in range(tenday + 1):
        res.append(f'movie-{year}-{month}-{i}')
    return res


def curTenDay():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    tenday = 0 if day < 10 else 1 if day < 20 else 2
    return f'movie-{year}-{month}-{tenday}'


def update(q, d):
    for word, cnt in d:
        q[word] = cnt + q.get(word, 0)


def get_hot_search_words():
    """
    [
    {'word': word, 'hot': hot}
    ]
    """
    # q = r.zrangebyscore(name='search_rank', min=0, max=100, withscores=True)
    # return [{'word': i[0].decode("utf-8")[:10], 'hot': i[1]} for i in reversed(q)][:10]
    res = []
    q = {}
    for key in lastThreeTenDays():
        update(q, r.zrangebyscore(name=key, min=0, max=100, withscores=True))
    t = list(sorted(q.items(), key=lambda i: i[1], reverse=True))[:10]
    for word, cnt in t:
        res.append({'word': word, 'hot': cnt})
    return res


def search(w, ip):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if not (
            ip and r.sismember(f'movie-ip-search-{year}-{month}-{day}', f'{ip} {w}')
    ):
        r.sadd(f'movie-ip-search-{year}-{month}-{day}', f'{ip} {w}')
        r.expire(f'movie-ip-search-{year}-{month}-{day}', oneDay)
        key = curTenDay()
        r.zincrby(key, 1, w)
        r.expire(key, oneMonth)


def getMoviesByUrls(urls):
    if not urls: return []
    n = len(urls)
    res = [{} for _ in range(n)]
    values = list(r.hmget('movies', urls))
    for i in range(n):
        res[i]['url'] = urls[i]
        if not values[i]:
            res[i]['name'] = ''
        elif values[i].startswith('{'):
            res[i].update(json.loads(values[i]))
        else:
            res[i]['name'] = values[i]
    return res


def subscribeKeywords(mail, keywords):
    keywords = keywords.split()[:50]
    keywords.sort(key=lambda i: -len(i))
    t = []
    for w in keywords:
        if all(w not in word for word in t):
            t.append(w)
    keywords = t
    r.hset('movie_keywords_subscribe', mail, ' '.join(keywords))


if __name__ == '__main__':
    getMoviesByUrls(['https://www.jpysvip.net/voddetail/63064.html'])
    res = r.hget('movies', 'https://hanmiys.com/voddetail/119280.html')
    print(res)
    res = r.hmget('movies', ['https://hanmiys.com/voddetail/119280.html', 'https://www.wanmeikk.me/project/1985.html'])
    print(res)
    print(lastThreeTenDays())
    print(lastMonthTenDays())
    print(curTenDay())
    print(get_hot_search_words())
    search("盗墓笔记")
