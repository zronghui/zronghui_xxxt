#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import pretty_errors
from elasticsearch import Elasticsearch
import hashlib


# 计算密码的md5值
from loguru import logger


def get_md5(s):
    md = hashlib.md5()
    md.update(s.encode('utf-8'))
    return md.hexdigest()


es = Elasticsearch()
mapping = {
    'properties': {
        'title': {
            'type': 'text',
            'analyzer': 'ik_max_word',
            'search_analyzer': 'ik_max_word'
        }
    }
}
es.indices.delete(index='news', ignore=[400, 404])
es.indices.create(index='news', ignore=400)
result = es.indices.put_mapping(index='news', doc_type='politics', body=mapping)
logger.debug(result)
# {'acknowledged': True}

datas = [
    {
        'title': '美国留给伊拉克的是个烂摊子吗',
        'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
        'date': '2011-12-16'
    },
    {
        'title': '公安部：各地校车将享最高路权',
        'url': 'http://www.chinanews.com/gn/2011/12-16/3536077.shtml',
        'date': '2011-12-16'
    },
    {
        'title': '中韩渔警冲突调查：韩警平均每天扣1艘中国渔船',
        'url': 'https://news.qq.com/a/20111216/001044.htm',
        'date': '2011-12-17'
    },
    {
        'title': '中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首',
        'url': 'http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml',
        'date': '2011-12-18'
    },
    {
        'title': '中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首',
        'url': 'http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml',
        'date': '2011-12-18'
    }
]

for data in datas:
    debug = es.index(index='news', doc_type='politics', body=data, id=get_md5(data['url']))
es.indices.refresh(index="news")

result = es.search(index='news', doc_type='politics')

logger.debug(json.dumps(result, indent=2, ensure_ascii=False))

dsl = {
    'query': {
        'match': {
            'title': '中国'
        }
    }
}

es = Elasticsearch()
# result = es.search(index='news', doc_type='politics', q='中国 领事馆')
result = es.search(index='news', doc_type='politics', body=dsl)

logger.debug(json.dumps(result, indent=2, ensure_ascii=False))

# {'acknowledged': True}
# {
#   "took": 3,
#   "timed_out": false,
#   "_shards": {
#     "total": 5,
#     "successful": 5,
#     "skipped": 0,
#     "failed": 0
#   },
#   "hits": {
#     "total": 4,
#     "max_score": 1.0,
#     "hits": [
#       {
#         "_index": "news",
#         "_type": "politics",
#         "_id": "q4xHqnABU_ZbTbliQ7pZ",
#         "_score": 1.0,
#         "_source": {
#           "title": "中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首",
#           "url": "http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml",
#           "date": "2011-12-18"
#         }
#       },
#       {
#         "_index": "news",
#         "_type": "politics",
#         "_id": "qoxHqnABU_ZbTbliQ7pQ",
#         "_score": 1.0,
#         "_source": {
#           "title": "中韩渔警冲突调查：韩警平均每天扣1艘中国渔船",
#           "url": "https://news.qq.com/a/20111216/001044.htm",
#           "date": "2011-12-17"
#         }
#       },
#       {
#         "_index": "news",
#         "_type": "politics",
#         "_id": "qIxHqnABU_ZbTbliQ7oy",
#         "_score": 1.0,
#         "_source": {
#           "title": "美国留给伊拉克的是个烂摊子吗",
#           "url": "http://view.news.qq.com/zt2011/usa_iraq/index.htm",
#           "date": "2011-12-16"
#         }
#       },
#       {
#         "_index": "news",
#         "_type": "politics",
#         "_id": "qYxHqnABU_ZbTbliQ7pJ",
#         "_score": 1.0,
#         "_source": {
#           "title": "公安部：各地校车将享最高路权",
#           "url": "http://www.chinanews.com/gn/2011/12-16/3536077.shtml",
#           "date": "2011-12-16"
#         }
#       }
#     ]
#   }
# }
# {
#   "took": 7,
#   "timed_out": false,
#   "_shards": {
#     "total": 5,
#     "successful": 5,
#     "skipped": 0,
#     "failed": 0
#   },
#   "hits": {
#     "total": 2,
#     "max_score": 0.2876821,
#     "hits": [
#       {
#         "_index": "news",
#         "_type": "politics",
#         "_id": "q4xHqnABU_ZbTbliQ7pZ",
#         "_score": 0.2876821,
#         "_source": {
#           "title": "中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首",
#           "url": "http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml",
#           "date": "2011-12-18"
#         }
#       },
#       {
#         "_index": "news",
#         "_type": "politics",
#         "_id": "qoxHqnABU_ZbTbliQ7pQ",
#         "_score": 0.2876821,
#         "_source": {
#           "title": "中韩渔警冲突调查：韩警平均每天扣1艘中国渔船",
#           "url": "https://news.qq.com/a/20111216/001044.htm",
#           "date": "2011-12-17"
#         }
#       }
#     ]
#   }
# }
#
