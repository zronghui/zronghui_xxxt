#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pretty_errors
import requests
from loguru import logger
import re
import json
import itertools

import config

pretty_errors.activate()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/8'
                         '1.0.4044.122 Safari/537.36'}


def getMovieId(q, apikey):
    try:
        r = requests.get('https://api.douban.com/v2/movie/search?q={q}&apikey={apikey}'.
                         format(q=q, apikey=apikey),
                         headers=headers)
        return r.json()['subjects'][0]['id']
    except Exception as e:
        # api 请求失败，直接发送请求
        logger.error(e)
        r = requests.get('https://www.douban.com/search?q='+q, headers=headers)
        return re.findall(r'com%2Fsubject%2F(.*?)%2F', r.text)[0]


def getMovieDetail(movie_id, apikey):
    r = requests.get('https://api.douban.com/v2/movie/subject/{movie_id}?apikey={apikey}'.
                     format(movie_id=movie_id, apikey=apikey),
                     headers=headers)
    if 'id' in r.json():
        return r.json()
    # api 请求失败，直接发送请求
    r = requests.get('https://movie.douban.com/subject/' +
                     str(movie_id), headers=headers)
    r = json.loads(re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                              r.text.replace('\n', ''))[0])
    # print(json.dumps(r, ensure_ascii=False, indent=2))
    for i in itertools.chain(r['director'], r['actor']):
        for j in i:
            i['name'] = i['name'].split()[0]
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
    return res


def getMovieDetailByQuery(q):
    try:
        movie_id = getMovieId(q, config.doubanApikey)
        return getMovieDetail(movie_id, config.doubanApikey)
    except Exception as e:
        logger.error(e)


# def main():
#     q = '余欢水'
#     movie_id = getMovieId(q, config.doubanApikey)
#     logger.debug(movie_id)
#     logger.debug(getMovieDetail(movie_id, config.doubanApikey))

if __name__ == '__main__':
    print(getMovieDetail(getMovieId('摩天大楼', ''), ''))
