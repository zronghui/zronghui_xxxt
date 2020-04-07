#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint

import pretty_errors
from elasticsearch import Elasticsearch

es = Elasticsearch()
pretty_errors.activate()


def search(q, _from=0):
    dsl = {"query":
               {"bool":
                    {"must": [],
                     "must_not": [],
                     "should": []}
                },
           "from": _from,
           "size": 10,
           "highlight": {
               "pre_tags": ['<span class="highlight">'],
               "post_tags": ['</span>'],
               "fields": {
                   "book_name": {}
               }
           },
           "sort": [],
           "aggs": {},
           "version": True
           }
    for i in q.split():
        dsl["query"]["bool"]["should"].append({"wildcard": {"book_name": i}})
    result = es.search(index='books', doc_type='books', body=dsl)
    return result


if __name__ == '__main__':
    # es.indices.refresh(index="news")
    pprint(search('健身 mobi', _from=20))
