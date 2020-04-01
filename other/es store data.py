#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from itertools import chain

import pretty_errors
from elasticsearch import Elasticsearch, helpers

pretty_errors.activate()

es = Elasticsearch()

# 建立index
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

# 批量插入数据
print("============== index ================")
count = 0
i = 0
j = 0
num = 0
actions = []
max_count = 2000
with open('shudan1.json', 'r', encoding='utf-8') as f1, open('volmoe1.json', 'r', encoding='utf-8') as f2:
    for line in chain(f1, f2):
        j += 1
        try:
            triple_dict = json.loads(line)
            # 如果数据量小可以用index的方法一条条插入
            # 这里index，doc_type就等于上一步建立索引所用的名称
            # es.index(index='index_test',doc_type='doc_type',body=triple_dict)
            action = {
                "_index": "books",
                "_type": "books",
                # "_id": i,
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
