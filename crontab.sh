#!/usr/bin/env bash

cd helloScrapy || exit
scrapy crawl books
scrapy crawl movies
cd ../other || exit
python3 es\ store\ data.py
# 0 */1 * * * cd $xxxt && ./crontab.sh >> $xxxt/crontab.log 2>&1
