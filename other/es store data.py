#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

import pretty_errors
from elasticsearch import Elasticsearch, helpers
import hashlib


# 计算密码的md5值
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
    print(result)

    es.indices.delete(index='movies', ignore=[400, 404])
    es.indices.create(index='movies', ignore=400)
    result = es.indices.put_mapping(index='movies', doc_type='movies', body=mapping)
    print(result)


def bulk_with_json(jsonFile, doc_type):
    # 批量插入数据
    print(f"============== bulk with {jsonFile} ================")
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
                d = json.loads(line)
                if not d.get('_source'):
                    triple_dict = d
                else:
                    triple_dict = d.get('_source')
                triple_dict['book_name_length'] = len(triple_dict['book_name'])
                # 如果数据量小可以用index的方法一条条插入
                # 这里index，doc_type就等于上一步建立索引所用的名称
                # es.index(index='index_test',doc_type='doc_type',body=triple_dict)
                action = {
                    "_index": doc_type,
                    "_type": doc_type,
                    "_id": d['_id'] if d['_id'] else get_md5(triple_dict['book_url']),
                    "_source": triple_dict
                }
                i += 1
                count += 1
                actions.append(action)
            except:
                print(f"!!! {j} th row insert faied: {line}")
                continue
            if count >= max_count:
                helpers.bulk(es, actions)
                actions = []
                count = 0
                num += 1
                print("Insert " + str(num * max_count) + " records.")
    helpers.bulk(es, actions)
    print('finish~~~')


if __name__ == '__main__':
    bulk_with_json(jsonFile='../helloScrapy/books.json', doc_type='books')
    bulk_with_json(jsonFile='../helloScrapy/movies.json', doc_type='movies')
    os.system('rm ../helloScrapy/books.json; rm ../helloScrapy/movies.json')

    # 建立index
    # build_index()
    # bulk_with_json(jsonFile='../movies.json', doc_type='books')
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
