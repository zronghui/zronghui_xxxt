#!/usr/bin/env bash

export InCrontab=true

#python other/checkService.py
cd helloScrapy || exit

while true
do
    echo 'scrapy begin...'
    scrapy crawl movies
    for i in `seq 1 300`
    do
        echo -n 'sleep '$i'/300s...'
        sleep 1
    done
done
