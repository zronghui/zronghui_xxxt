### 安装、自启动


？

### 开启

```shell
nginx -c /etc/nginx/nginx.conf # 必须是绝对路径
```



### 重新加载

```shell
nginx -s reload
```



### 核心配置

```shell
# 静态文件设置
# zronghui_xxxt/nginx/nginxconfig.io/general.conf
location /static/ {
    add_header Cache-Control public;
    alias /root/zronghui_xxxt/SearchWeb/static/;
}

# reverse proxy
# zronghui_xxxt/nginx/sites-available/101.200.240.225.conf
location /search {
  proxy_pass http://127.0.0.1:8033;
  include    nginxconfig.io/proxy.conf;
}
```

site-enabled 中的文件都是 site-available 中文件的软链接