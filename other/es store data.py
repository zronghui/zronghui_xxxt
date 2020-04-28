#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import json
import os

import pretty_errors
from elasticsearch import Elasticsearch, helpers
from environs import Env
from loguru import logger


def get_md5(s):
    md = hashlib.md5()
    md.update(s.encode('utf-8'))
    return md.hexdigest()


pretty_errors.activate()

es = Elasticsearch()


def build_index():
    mapping = {
        'properties': {
            'book_name': {
                'type': 'text',
                'analyzer': 'ik_max_word',
                'search_analyzer': 'ik_max_word'
            }
        }
    }
    es.indices.delete(index='books', ignore=[400, 404])
    es.indices.create(index='books', ignore=400)
    result = es.indices.put_mapping(index='books', doc_type='books', body=mapping)
    logger.debug(result)

    es.indices.delete(index='movies', ignore=[400, 404])
    es.indices.create(index='movies', ignore=400)
    result = es.indices.put_mapping(index='movies', doc_type='movies', body=mapping)
    logger.debug(result)


def bulk_with_json(jsonFile, doc_type):
    # 批量插入数据
    logger.debug(f"bulk with {jsonFile}")
    count = 0
    i = 0
    j = 0
    num = 0
    actions = []
    max_count = 2000
    with open(jsonFile, 'r', encoding='utf-8') as f:
        for line in f:
            j += 1
            try:
                action, triple_dict = getAction(doc_type, line)
                i += 1
                count += 1
                actions.append(action)
            except Exception as e:
                logger.error(e)
                logger.debug(f"!!! {j} th row insert faied: {triple_dict}")
                continue
            if count >= max_count:
                bulk(actions)
                actions = []
                count = 0
                num += 1
                logger.debug("Insert " + str(num * max_count) + " records.")
    bulk(actions)
    logger.debug('finish~~~')


def bulk(actions):
    try:
        helpers.bulk(es, actions)
    except Exception as e:
        logger.error(e)
        for action in actions:
            try:
                es.index(index=action['_index'], doc_type=action['_type'],
                         body=action["_source"],
                         id=action['_id'])
            except Exception as e:
                logger.error(e)


def getAction(doc_type, line):
    d = json.loads(line)
    if not d.get('_source'):
        triple_dict = d
    else:
        triple_dict = d.get('_source')
    triple_dict['book_name_length'] = triple_dict.get('book_name_length', len(triple_dict['book_name']))
    # 如果数据量小可以用index的方法一条条插入
    # 这里index，doc_type就等于上一步建立索引所用的名称
    # es.index(index='index_test',doc_type='doc_type',body=triple_dict)
    action = {
        "_index": doc_type,
        "_type": doc_type,
        "_id": d.get('_id') if d.get('_id') else get_md5(triple_dict['book_url']),
        "_source": triple_dict
    }
    return action, triple_dict


if __name__ == '__main__':
    env = Env()
    env.read_env()
    InCrontab = env.bool("InCrontab", False)
    if InCrontab:
        book = 'CrontabBooks.json'
        movie = 'CrontabMovies.json'
    else:
        book = 'books.json'
        movie = 'movies.json'
    bulk_with_json(jsonFile='../helloScrapy/' + book, doc_type='books')
    bulk_with_json(jsonFile='../helloScrapy/' + movie, doc_type='movies')
    os.system('rm ../helloScrapy/' + book)
    os.system('rm ../helloScrapy/' + movie)

    # 建立index
    # build_index()
    # bulk_with_json(jsonFile='../movies.json', doc_type='movies')
    # bulk_with_json(jsonFile='../books.json', doc_type='books')

    # bulk_with_json(jsonFile='axcs.json', doc_type='books')
    # bulk_with_json(jsonFile='bttwo.json', doc_type='movies')
    # bulk_with_json(jsonFile='ddrk.json', doc_type='movies')
    # bulk_with_json(jsonFile='dvdhd.json', doc_type='movies')
    # bulk_with_json(jsonFile='itsck.json', doc_type='movies')
    # bulk_with_json(jsonFile='java1234.json', doc_type='books')
    # bulk_with_json(jsonFile='shudan1.json', doc_type='books')
    # bulk_with_json(jsonFile='volmoe1.json', doc_type='books')
    # bulk_with_json(jsonFile='xiangzhan.json', doc_type='books')
    # bulk_with_json(jsonFile='zhenbuka.json', doc_type='movies')
