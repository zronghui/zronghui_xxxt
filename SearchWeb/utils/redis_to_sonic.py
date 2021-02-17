#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pretty_errors
from alive_progress import alive_bar
from sonic import IngestClient
from tenacity import retry, stop_after_attempt

import redis_utils

pretty_errors.activate()

ingestcl = IngestClient("8.136.0.121", '1491', "SecretPassword")
hash = redis_utils.r.hgetall('movies')


@retry(stop=stop_after_attempt(10))
def push_to_sonic(url, name):
    ingestcl.push(collection="movies", bucket="default",
                  object=url, text=name,
                  lang=None)


with alive_bar(total=len(hash)) as bar:
    for url in hash:
        name = hash.get(url)
        push_to_sonic(url, name)
        bar()
