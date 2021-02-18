#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import pretty_errors
import redis
import click
from icecream import ic

import sendQQMail

pretty_errors.activate()

host = '127.0.0.1'
port = 6379
r = redis.StrictRedis(host=host, port=port, password='redispassword', decode_responses=True, charset='utf-8')


@click.group()
def cli():
    pass


@cli.command("takeUpdate")
def takeUpdate():
    # r.rpush('movieUpdate', '{
    #         name:"乌龙院之活宝传奇 第二季",
    #         url: "https://hanmiys.com/voddetail/126877.html",
    #         desc:"52集全"
    #     }')

    print('takeUpdate')
    while True:
        try:
            ic('1. 从 movieUpdate blpop 取出更新的资源')
            # blpop 后形如 ('movieUpdate',
            #             '{name:"乌龙院之活宝传奇 第二季",url: '
            #             '"https://hanmiys.com/voddetail/126877.html",desc:"52集全"}')
            # the JSON object must be str, bytes or bytearray, not tuple
            # 所以需要取元组的第 2 个元素
            movie = r.blpop('movieUpdate')[1]
            movie = json.loads(movie)
            ic(movie)
            ic('2. 遍历所有 movie_keywords_subscribe 中的 mail -> keywords')
            for mail, keywords in r.hgetall('movie_keywords_subscribe').items():
                ic('3. 遍历所有的 keyword')
                for keyword in keywords.split():
                    # ic('4. 如果更新资源中包括 keyword, 添加到邮件通知的队列中')
                    if keyword in movie.get('name', ''):
                        # td = {'mail': mail, 'keyword': keyword}
                        # td.update(movie)
                        # r.rpush('movieMailNotify', json.dumps(dict(td), ensure_ascii=False))
                        # 直接发送邮件, 不放入其他队列了↑
                        url = movie.get('url')
                        name = movie.get('name')
                        desc = movie.get('desc')
                        ic("4. 发送邮件提醒", url, name, desc, keyword)
                        sendQQMail.mail(MyName='xxxt', head=f'{keyword}更新了-xxxt',
                                        content=f'<a href="{url}" target="_blank">{name} - {desc}</a>',
                                        to=mail)
        except Exception as e:
            print(e)


@cli.command("sendMail")
def sendMail():
    print('sendMail')
    while True:
        try:
            # 1. 从 movieMailNotify blpop 取出需要发送的邮件
            movie = json.loads(r.blpop('movieMailNotify'))
            # mail
        except Exception as e:
            pass


if __name__ == '__main__':
    cli()
