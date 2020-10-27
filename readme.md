



## 项目介绍

scrapy + elasticsearch + django 实现的影视搜索系统

演示地址：[101.200.240.225](http://101.200.240.225/search)  (暂时不可用。可能因为存的数据太多了，而且服务器是 1核 1G 的，elastic search 内存不够用，崩了)

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



## 定时爬虫

2种方式，之前用 crontab，现在用 supervisor

### 1.crontab

```
#!/bin/sh
PATH=/usr/local/bin:/usr/local/sbin:~/bin:/usr/bin:/bin:/usr/sbin:/sbin
xxxt=/root/code/zronghui_xxxt
InCrontab=true

# xxxt
# 5 分钟启动一次爬虫
*/5 * * * * cd $xxxt && ./crontab.sh
```

### 2.supervisor

```

[program:xxxt]
command=/usr/local/python3/bin/python3.8 manage.py runserver 0.0.0.0:8033 --insecure   ; 被监控的进程路径
directory=/root/code/zronghui_xxxt/SearchWeb               ; 执行前要不要先cd到目录去，一般不用
priority=1                    ;数字越高，优先级越高
numprocs=1                    ; 启动几个进程
autostart=true                ; 随着supervisord的启动而启动
autorestart=true
startretries=10               ; 启动失败时的最多重试次数
exitcodes=0                   ; 正常退出代码（是说退出代码是这个时就不再重启了吗？待确定）
stopsignal=KILL               ; 用来杀死进程的信号
stopwaitsecs=10               ; 发送SIGKILL前的等待时间
redirect_stderr=true          ; 重定向stderr到stdout

[program:xxxtScrapy]
enviroment=InCrontab=true ; 设置环境变量
command=job -s "*/5 * * * *" -- ./crontab.sh   ; 被监控的进程路径
directory=/root/code/zronghui_xxxt               ; 执行前要不要先cd到目录去，一般不用
priority=1                    ;数字越高，优先级越高
numprocs=1                    ; 启动几个进程
autostart=true                ; 随着supervisord的启动而启动
autorestart=false
startretries=10               ; 启动失败时的最多重试次数
exitcodes=0                   ; 正常退出代码（是说退出代码是这个时就不再重启了吗？待确定）
stopsignal=KILL               ; 用来杀死进程的信号
stopwaitsecs=10               ; 发送SIGKILL前的等待时间
redirect_stderr=true          ; 重定向stderr到stdout

```



## todo

1.网站起个名字、图标等等

```shell
ag lookao
```

2.存储每次请求的豆瓣信息 设置超时

3.用 Redis 存储豆瓣信息(id->json)

4.系统架构图？

5.搜索前查询 Redis es 服务的状态、自动检测服务，服务状态变化时邮件报错提醒



删除所有 es 的数据，只爬取优质的站点 (docker 中 es 的数据放在哪里，怎么删除)

爬取时设置列表页 和 获取下一页，并且可以用参数配置是否爬取下一页，用 Redis 存储 某站点 某分类最近爬取更新的 movie

页面改版，美化，前端 bug

搜索热榜逻辑  看其他搜索引擎怎么做的 -> 优化

把整个项目移到自己的服务器

去除书籍搜索功能

