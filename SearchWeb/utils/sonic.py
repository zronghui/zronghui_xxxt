#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sonic import SearchClient
import pretty_errors

pretty_errors.activate()

querycl = SearchClient("127.0.0.1", 1491, "SecretPassword")


def search(q, _from, doc_type):
    return querycl.query(collection=doc_type, bucket="default", terms=q, limit=20, offset=_from, lang=None)
# print(querycl.ping())
# print(querycl.query("wiki", "articles", "for"))
# print(querycl.query("wiki", "articles", "love"))
# print(querycl.query("wiki", "articles", "测试"))
# print(querycl.suggest("wiki", "articles", "helmet"))
