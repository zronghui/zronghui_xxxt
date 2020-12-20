#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sonic import IngestClient
import pretty_errors

pretty_errors.activate()

with IngestClient("106.75.229.2", 1491, "SecretPassword") as ingestcl:
    print(ingestcl.ping())
    print(ingestcl.protocol)
    print(ingestcl.bufsize)
    print(ingestcl.push(collection="wiki", bucket="default", object="article-1", text="for the love of god hell",
                        lang=None))  # "Chinese (Simplified)"
    print(ingestcl.push("wiki", "articles", "article-1", "for the love of god hell"))
    print(ingestcl.push("wiki", "articles", "article-2", "for the love of satan heaven"))
    print(ingestcl.push("wiki", "articles", "article-3", "for the love of lorde hello"))
    print(ingestcl.push("wiki", "articles", "article-4", "for the god of loaf helmet"))
    print(ingestcl.push("wiki", "articles", "article-4", "for the god of loaf helmet"))
    print(ingestcl.push("wiki", "articles", "article-4", "中文查询测试"))

# collection 数据库名
# bucket 表名
# object id
# text 要搜索的文本
# 搜索的时候根据返回的 objects 回其他数据库中查找数据（如 Redis MySQL）


# [竞赛 - 力扣 (LeetCode)](https://leetcode-cn.com/contest/weekly-contest-220)
# [检查边长度限制的路径是否存在 - 力扣 (LeetCode) 竞赛](https://leetcode-cn.com/contest/weekly-contest-220/problems/checking-existence-of-edge-length-limited-paths/)
# [Dijkstra 与 Floyd 算法 - boobo - 博客园](https://www.cnblogs.com/RB26DETT/p/11091198.html)
# [根据无向图的边邻接矩阵求任意一点到其他所有点之间的最短路径。 - fcyh - 博客园](https://www.cnblogs.com/yjd_hycf_space/p/7090660.html)
# [云主机 - Default](https://console.ucloud.cn/uhost/uhost?hpc=false)
# [基础网络 - Default](https://console.ucloud.cn/unet/ufirewall/firewall-5ny52ibj)
