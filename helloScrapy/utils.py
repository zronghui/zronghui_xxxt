#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import requests

proxypool_url = 'http://127.0.0.1:5555/random'


def get_random_proxy():
    """
    get random proxy from proxypool
    :return: proxy
    """
    proxy = requests.get(proxypool_url).text.strip()
    print(proxy)
    return 'http://' + proxy


def main():
    """
    main method, entry point
    :return: none
    """
    print(get_random_proxy())


def removeBookDesc():
    with open('Douban1.json', 'w', encoding='utf-8') as fw:
        with open('Douban.json', 'r', encoding='utf-8') as fr:
            for line in fr:
                item = json.loads(line.strip())
                if 'book_desc' in item:
                    del item['book_desc']
                fw.write(json.dumps(dict(item), ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
