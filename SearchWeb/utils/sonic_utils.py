#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sonic import SearchClient, IngestClient, ControlClient
import pretty_errors

pretty_errors.activate()

querycl = SearchClient("8.136.0.121", 1491, "SecretPassword")


def search(q, _from, doc_type, limit=20, lang=None):
    return querycl.query(collection=doc_type, bucket="default", terms=q, limit=limit, offset=_from, lang=lang)


def flush():
    # 清除数据
    with IngestClient("8.136.0.121", 1491, "SecretPassword") as ingestcl:
        ingestcl.flush(collection='movies')
# print(querycl.ping())
# print(querycl.query("wiki", "articles", "for"))
# print(querycl.query("wiki", "articles", "love"))
# print(querycl.query("wiki", "articles", "测试"))
# print(querycl.suggest("wiki", "articles", "helmet"))

if __name__ == '__main__':
    with ControlClient("8.136.0.121", 1491, "SecretPassword") as controlcl:
        print(controlcl.ping())
        controlcl.trigger("consolidate")
    print(search(q='斗罗大陆', _from=0, doc_type='movies'))
    
