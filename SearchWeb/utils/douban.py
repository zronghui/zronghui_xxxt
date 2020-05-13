#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pretty_errors
import requests
from loguru import logger

import config

pretty_errors.activate()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/8'
                         '1.0.4044.122 Safari/537.36'}


def getMovieId(q, apikey):
    r = requests.get('https://api.douban.com/v2/movie/search?q={q}&apikey={apikey}'.
                     format(q=q, apikey=apikey),
                     headers=headers)
    return r.json()['subjects'][0]['id']


def getMovieDetail(movie_id, apikey):
    r = requests.get('https://api.douban.com/v2/movie/subject/{movie_id}?apikey={apikey}'.
                     format(movie_id=movie_id, apikey=apikey),
                     headers=headers)
    return r.json()


def getMovieDetailByQuery(q):
    try:
        movie_id = getMovieId(q, config.doubanApikey)
        return getMovieDetail(movie_id, config.doubanApikey)
    except Exception as e:
        logger.error(e)


def main():
    q = '余欢水'
    movie_id = getMovieId(q, config.doubanApikey)
    logger.debug(movie_id)
    logger.debug(getMovieDetail(movie_id, config.doubanApikey))


if __name__ == '__main__':
    main()
