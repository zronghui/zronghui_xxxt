#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sonic import SearchClient, IngestClient
import pretty_errors

pretty_errors.activate()

querycl = SearchClient("8.136.0.121", 1491, "SecretPassword")


def search(q, _from, doc_type):
    return querycl.query(collection=doc_type, bucket="default", terms=q, limit=20, offset=_from, lang=None)


# print(querycl.ping())
# print(querycl.query("wiki", "articles", "for"))
# print(querycl.query("wiki", "articles", "love"))
# print(querycl.query("wiki", "articles", "测试"))
# print(querycl.suggest("wiki", "articles", "helmet"))

if __name__ == '__main__':
    print(search(q='斗罗大陆', _from=0, doc_type='movies'))
