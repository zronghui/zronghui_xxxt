#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pretty_errors
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from helloScrapy.spiders.gqzzw import GqzzwSpider

pretty_errors.activate()

l = [
    ('http://www.gqzzw.com/type/zrcs/1', '做人与处世'),
    # 意林
    ('http://www.gqzzw.com/type/jias/1', '意林/意林·原创版讲述'),
    ('http://www.gqzzw.com/type/yili/1', '意林/意林'),
    ('http://www.gqzzw.com/type/yiln/1', '意林/意林·12+'),
    ('http://www.gqzzw.com/type/ylsn/1', '意林/意林·少年版'),
    # 读者
    ('http://www.gqzzw.com/type/dzxy/1', '读者/读者·校园版'),
    ('http://www.gqzzw.com/type/duzh/1', '读者/读者'),
    ('http://www.gqzzw.com/type/dzyc/1', '读者/读者·原创版'),
    # 健康养生食品
    ('http://www.gqzzw.com/type/ptzs/1', '健康养生食品/烹调知识·原创版'),
    ('http://www.gqzzw.com/type/spsh/1', '健康养生食品/食品与生活'),
    ('http://www.gqzzw.com/type/dzjk/1', '健康养生食品/大众健康'),
    ('http://www.gqzzw.com/type/znjk/1', '健康养生食品/祝您健康'),
    ('http://www.gqzzw.com/type/spji/1', '健康养生食品/食品界'),
    ('http://www.gqzzw.com/type/rsjk/1', '健康养生食品/饮食与健康·下旬刊'),
    ('http://www.gqzzw.com/type/bjsh/1', '健康养生食品/保健与生活'),
    ('http://www.gqzzw.com/type/klys/1', '健康养生食品/家庭医药·快乐养生'),
    ('http://www.gqzzw.com/type/jtyi/1', '健康养生食品/家庭医药'),
    ('http://www.gqzzw.com/type/jkbl/1', '健康养生食品/健康博览'),
    ('http://www.gqzzw.com/type/dzyx/1', '健康养生食品/大众医学'),
    ('http://www.gqzzw.com/type/bjzn/1', '健康养生食品/养生保健指南'),
    # 计算机
    ('http://www.gqzzw.com/type/jssw/1', '计算机/计算机应用文摘·触控'),
    ('http://www.gqzzw.com/type/zsjs/1', '计算机/电脑知识与技术·经验技巧'),
]

for lastPage, zzname in l:
    os.system(f"scrapy crawl gqzzw -a lastPage='{lastPage}' -a zzname='{zzname}'")
# process = CrawlerProcess(get_project_settings())
# for lastPage, zzname in l:
#     process.crawl(GqzzwSpider, lastPage=lastPage, zzname=zzname)
# process.start()
