#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pretty_errors
import requests
from loguru import logger
import re
import json
import itertools
import functools
import funcy
from utils import redis_utils

# import config

pretty_errors.activate()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/8'
                         '1.0.4044.122 Safari/537.36'}


@funcy.print_durations
@funcy.print_exits
@functools.lru_cache(maxsize=128)
def getMovieId(q):
    # try:
    #     r = requests.get('https://api.douban.com/v2/movie/search?q={q}&apikey={apikey}'.
    #                      format(q=q, apikey=apikey),
    #                      headers=headers)
    #     return r.json()['subjects'][0]['id']
    # except Exception as e:
    # # api 请求失败，直接发送请求
    # logger.error(e)
    res = redis_utils.r.hget('movieQueryToMovieId', q)
    if res:
        return res
    r = requests.get('https://www.douban.com/search?q=' + q, headers=headers)
    res = re.findall(r'com%2Fsubject%2F(.*?)%2F', r.text)[0]
    redis_utils.r.hset('movieQueryToMovieId', q, res)
    return res


@funcy.print_durations
@functools.lru_cache(maxsize=128)
def getMovieDetail(movie_id):
    # r = requests.get('https://api.douban.com/v2/movie/subject/{movie_id}?apikey={apikey}'.
    #                  format(movie_id=movie_id, apikey=apikey),
    #                  headers=headers)
    # if 'id' in r.json():
    #     return r.json()
    # # api 请求失败，直接发送请求

    res = redis_utils.r.hget('movieDesc', movie_id)
    if res:
        res = json.loads(res)
        return res

    r = requests.get('https://movie.douban.com/subject/' +
                     str(movie_id), headers=headers)
    r = json.loads(re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                              r.text.replace('\n', ''))[0])
    # print(json.dumps(r, ensure_ascii=False, indent=2))
    for i in itertools.chain(r['director'], r['actor']):
        i['name'] = ' '.join(i['name'].split()[:1])
    res = {
        'title': r['name'],
        'id': str(movie_id),
        'rating': {'average': r['aggregateRating']['ratingValue']},
        'year': r['datePublished'].split('-', 1)[0],
        'genres': r['genre'],
        'images': {'medium': r['image']},
        'summary': r['description'],
        'directors': r['director'],
        'casts': r['actor']
    }
    redis_utils.r.hset('movieDesc', movie_id, json.dumps(res))
    return res


def getMovieDetailByQuery(q):
    try:
        movie_id = getMovieId(q)
        return getMovieDetail(movie_id)
    except Exception as e:
        logger.error(e)


# def main():
#     q = '余欢水'
#     movie_id = getMovieId(q, config.doubanApikey)
#     logger.debug(movie_id)
#     logger.debug(getMovieDetail(movie_id, config.doubanApikey))

if __name__ == '__main__':
    print(getMovieDetail(getMovieId('摩天大楼')))
    print(getMovieDetailByQuery("斗罗大陆"))
