#!/usr/bin/env bash

cd helloScrapy || exit
scrapy crawl books
scrapy crawl movies
cd ../other || exit
python3 es\ store\ data.py

# crontab -e
# xxxt=/root/code/zronghui_xxxt
# 0 */1 * * * cd $xxxt && ./crontab.sh >> $xxxt/crontab.log 2>&1