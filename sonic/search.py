#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sonic import SearchClient
import pretty_errors

pretty_errors.activate()

with SearchClient("106.75.229.2", 1491, "SecretPassword") as querycl:
    print(querycl.ping())
    print(querycl.query("wiki", "articles", "for"))
    print(querycl.query("wiki", "articles", "love"))
    print(querycl.query("wiki", "articles", "测试"))
    print(querycl.suggest("wiki", "articles", "helmet"))

# True
# []
# ['article-3', 'article-2', 'article-1']
# ['article-4']
# PENDING SijGTX6r
