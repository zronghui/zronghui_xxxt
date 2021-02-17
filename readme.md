



## 项目介绍

scrapy + [sonic🦔 ](https://github.com/valeriansaliou/sonic) + django 实现的简单的影视搜索系统

演示地址：[8.136.0.121/search](http://8.136.0.121/search)  

sonic: 🦔 Fast, lightweight & schema-less search backend. An alternative to Elasticsearch that runs on a few MBs of RAM.(fuck es)



数据获取：爬取 movie_url 和 movie_name, 存储到 redis 中的字典，movie_url -> movie_name，同时存入 sonic 中。

数据搜索：从 sonic 中获取搜索出的 movie_urls（sonic 只存储主键），再去 Redis 中查询出 movie_names.

## 添加新的网站爬虫

![KpZnT2herAxIFmf](https://i.loli.net/2020/05/05/KpZnT2herAxIFmf.png)



![PEyDcpuSXRro3Ke](https://i.loli.net/2020/05/05/PEyDcpuSXRro3Ke.png)

