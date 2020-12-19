#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from sendQQMail import mail


def check(serviceName, serviceUrl):
    try:
        error = requests.get(serviceUrl).status_code != 200
    except:
        error = True
    if error:
        mail(
            myName="service check",
            head=f"{serviceName} error",
            content=f'{serviceName} {serviceUrl}'
        )


if __name__ == '__main__':
    check("redis", "http://127.0.0.1:6379")
    check("ElasticSearch", "http://127.0.0.1:9200")
