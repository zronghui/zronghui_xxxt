#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint

import jieba
import pretty_errors
from elasticsearch import Elasticsearch

es = Elasticsearch()
pretty_errors.activate()


def search(q, _from=0, doc_type=None):
    dsl = {"query":
               {"bool":
                    {"must": [],
                     "must_not": [],
                     "should": []}
                },
           "from": _from,
           "size": 20,
           "highlight": {
               "pre_tags": ['<span class="highlight">'],
               "post_tags": ['</span>'],
               "fields": {
                   "book_name": {}
               }
           },
           "sort": [
               {"_score": {"order": "desc"}},  # desc asc
               {"book_name_length": {'order': 'asc', "missing": "_last", "ignore_unmapped": True}},
               # 为什么用 script 一直不生效？
               # {
               #     "_script": {
               #         "script": "doc['book_name'].value.length()",
               # # str: length() array: size()
               #         "type": "number",
               #         "order": "asc"
               #     }
               # }
           ],
           "aggs": {},
           "version": True
           }
    # 1. 包含所有字
    for i in q.replace(' ', ''):
        dsl["query"]["bool"]["must"].append({"wildcard": {"book_name": i}})
    result = es.search(index=doc_type, doc_type=doc_type, body=dsl)
    if result['hits']['total'] != 0:
        return result
    dsl["query"]["bool"]["must"] = []
    # 2. jieba 分词
    q.replace('的', '')
    search_words = list(set(jieba.cut_for_search(q)))
    for i in search_words:
        dsl["query"]["bool"]["should"].append({"wildcard": {"book_name": i}})
    result = es.search(index=doc_type, doc_type=doc_type, body=dsl)
    if result['hits']['total'] != 0:
        return result
    # 3. 逐字拆解
    dsl["query"]["bool"]["should"] = []
    for i in q:
        dsl["query"]["bool"]["should"].append({"wildcard": {"book_name": i}})
    result = es.search(index=doc_type, doc_type=doc_type, body=dsl)
    return result


if __name__ == '__main__':
    # es.indices.refresh(index="news")
    pprint(search('健身 mobi', _from=20))
