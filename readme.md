



## 项目介绍

scrapy + elasticsearch + django 实现的影视搜索系统

演示地址：[47.93.53.47](http://47.93.53.47/)

也有书籍搜索系统，也可以添加其他类型的搜索系统

## 启动项目

```shell
j xxxt
tmux new -t xxxt
python manage.py runserver 0.0.0.0:80 --insecure
```

## 添加新的网站爬虫

![KpZnT2herAxIFmf](https://i.loli.net/2020/05/05/KpZnT2herAxIFmf.png)



![PEyDcpuSXRro3Ke](https://i.loli.net/2020/05/05/PEyDcpuSXRro3Ke.png)



### 服务器爬取并存储到 es

```shell
j xxxt
git pull
cd helloScrapy
tmux new -t scrapy
scrapy crawl movies >> scrapy.log 2>&1
..
cd other
python es\ store\ data.py
```



### crontab 爬虫

```
#!/bin/sh
PATH=/usr/local/bin:/usr/local/sbin:~/bin:/usr/bin:/bin:/usr/sbin:/sbin
xxxt=/root/code/zronghui_xxxt
InCrontab=true

# xxxt
# 5 分钟启动一次爬虫
*/5 * * * * cd $xxxt && ./crontab.sh >> $xxxt/crontab.log 2>&1
# 2 小时删除一次日志
0 */2 * * * cd $xxxt && rm crontab.log

# 学校每日上报
*/1 * * * * ~/dailyreport.1m.sh
# 摘星 每日签到
0 */2 * * * cd /root/code/ssr_autocheckin && python3 main.py
# redis 开机自启
@reboot redis-server /usr/local/redis/etc/redis.conf
```



## todo

网站起个名字、图标等等

```shell
ag lookao
```

