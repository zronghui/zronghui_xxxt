#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sonic import IngestClient

import redis_utils, sonic_utils
import pretty_errors
from alive_progress import alive_bar
from tenacity import retry, stop_after_attempt

pretty_errors.activate()

ingestcl = IngestClient("101.200.240.225", '1491', "SecretPassword")
hash = redis_utils.r.hgetall('movies')


@retry(stop=stop_after_attempt(10))
def push_to_sonic(url, name):
    ingestcl.push(collection="movies", bucket="default",
                  object=url, text=name,
                  lang=None)


with alive_bar(total=len(hash)) as bar:
    for url in hash:
        name = str(hash.get(url).decode("utf-8"))
        url = str(url.decode("utf-8"))
        # print(url, type(url))
        # print(name, type(name))
        push_to_sonic(url, name)
        bar()
