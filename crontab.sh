#!/usr/bin/env bash

InCrontab=true

#python other/checkService.py
cd helloScrapy || exit

while true
do
    echo 'scrapy begin...'
    scrapy crawl movies
    for i in seq(1 300)
    do
        echo 'sleep '$i'/300s'
        sleep 1
    done
done
#cd ../other || exit
#python3 es\ store\ data.py

# crontab -e
# xxxt=/root/code/zronghui_xxxt
# 0 */1 * * * cd $xxxt && ./crontab.sh >> $xxxt/crontab.log 2>&1
