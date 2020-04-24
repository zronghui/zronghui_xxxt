#!/usr/bin/env bash

cd helloScrapy || exit
scrapy crawl books
scrapy crawl movies
cd ../other || exit
python es\ store\ data.py
