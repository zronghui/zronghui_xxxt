start_urls_v1 = [
	# 超清
	# *[f'https://www.mdoutv.com/movie_bt/page/{i}' for i in range(1, 188)],
	*[f'https://www.wanmeikk.me/category/{_type}-{pageNo}.html'
	  for _type, n in [(1, 30), (2, 10), (3, 3), (4, 3), (5, 12), (6, 8), (7, 1), (8, 1), (9, 1), (10, 1)]
	  for pageNo in range(n + 1)],
	*[f'https://www.jpysvip.net/vodtype/{_type}-{i}.html'
	  for _type, n in [(1, 676), (2, 217), (3, 30), (4, 102)]
	  for i in range(n + 1)],
	*[f'https://hanmiys.com/vodtype/{_type}-{i}.html'
	  for _type, n in [(1, 764), (2, 333), (3, 77), (4, 183)]
	  for i in range(n + 1)],
	*[f'https://www.zhenbuka.com/vodtype/{_type}-{i}.html'
	  for _type, n in [(1, 774), (2, 363), (3, 46), (4, 100)]
	  for i in range(n + 1)],
	# 动漫
	*[f'http://agefans.org/catalog?page={i}' for i in range(1, 208)],
	*[f'http://www.bimiacg.com/type/{_type}-{i}/'
	  for _type, n in [('juchang', 15), ('fanzu', 65), ('guoman', 6), ('riman', 6)]
	  for i in range(n + 1)],
	*[f'http://www.dmdm2020.com/dongmantype/{_type}/page/{i}.html'
	  for _type, n in [(20, 31), (21, 3)]
	  for i in range(n + 1)],
	*[f'http://www.yhdm.io/{_type}/{i}.html'
	  for _type, n in [('japan', 108), ('china', 22), ('american', 7), ('movie', 12)]
	  for i in range(n + 1)],
	*[f'http://www.yxdm.me/resource/15-{i}.html' for i in range(1, 134)],
	# 美剧
	# *[f'https://www.meijumi.net/usa/page/{i}' for i in range(1, 259)],
	# *[f'https://www.meijutt.tv/{i}_______.html' for i in range(1, 360)],
	# 剧情
	*[f'https://www.juqingba.cn/dianshiju/list_25_{i}.html' for i in range(1, 100)],  # omg 总共 1739页
	*[f'http://www.yue365.com/tv/neidi/index_{i}.shtml' for i in range(1, 100)],
]
start_urls_v2 = [
	# 2021 02 19
	# 动漫
	*[f'https://www.agefans.net/update?page={i}' for i in range(1, 121)],
	# [ZzzFun 动漫视频网 - (￣﹃￣)~zZZ - 最新日本动漫 - 推荐日本动漫 - 第 65 页](http://www.zzzfun.com/vod_type_id_1_page_65.html)
	# [ZzzFun 动漫视频网 - (￣﹃￣)~zZZ - 最新当季新番 - 推荐当季新番 - 第 7 页](http://www.zzzfun.com/vod_type_id_42_page_7.html)
	# [ZzzFun动漫视频网 - (￣﹃￣)~zZZ-最新剧场版OVA-推荐剧场版OVA-第14页](http://www.zzzfun.com/vod_type_id_3_page_14.html)
	*[f'http://www.zzzfun.com/vod_type_id_{_type}_page_{i}.html'
	  for _type, n in [(1, 65), (3, 14), (42, 7)]
	  for i in range(n + 1)],
]
start_urls_v3 = [
	# 2021 02 22
	# 超清
	# [1080 影视 - 超清电影 - 1080 影视 - 电影电视剧免费看](https://www.ak1080.com/vodtype/1-877.html)
	# [1080 影视 - 超清电影 - 1080 影视 - 电影电视剧免费看](https://www.ak1080.com/vodtype/2-412.html)
	# [1080 影视 - 超清电影 - 1080 影视 - 电影电视剧免费看](https://www.ak1080.com/vodtype/3-36.html)
	# [1080 影视 - 超清电影 - 1080 影视 - 电影电视剧免费看](https://www.ak1080.com/vodtype/4-109.html)
	*[f'https://www.ak1080.com/vodtype/{_type}-{i}.html'
	  for _type, n in [(1, 877), (2, 412), (3, 36), (42, 109)]
	  for i in range(n + 1)],
	# [【日本动漫】- 奇奇动漫 第 532 页](https://www.qiqidongman.com/vod-search-order-vod_addtime-area-%E6%97%A5%E6%9C%AC-p-532.html)
	# [【国产动漫】- 奇奇动漫 第 149 页](https://www.qiqidongman.com/vod-search-order-vod_addtime-area-%E5%9B%BD%E4%BA%A7-p-149.html)
	*[f'https://www.qiqidongman.com/vod-search-order-vod_addtime-area-{_type}-p-{i}.html'
		for _type, n in [('%E6%97%A5%E6%9C%AC', 532), ('%E5%9B%BD%E4%BA%A7', 149)]
		for i in range(n + 1)],
	# [最新连载 - 推荐连载 - 新时空动漫](https://www.xskdm.com/vodshow/1--------3---.html)
	# [最新动漫电影 - 新时空动漫](https://www.xskdm.com/vodtype/2-2.html)
	# [完结动漫 - 新时空动漫](https://www.xskdm.com/vodtype/3-7.html)
	*[f'https://www.xskdm.com/vodtype/{_type}-{i}.html'
	  for _type, n in [(2, 2), (3, 7)]
	  for i in range(n + 1)],
	*[f'https://www.xskdm.com/vodtype/1--------{i}---.html' for i in range(1, 3+1)],
  ]
start_urls_v4 = [
	# 2021 02 22
	# 4k
	# [最新电影 - 推荐电影 - 4K 鸭奈飞资源站 - 一个专做奈飞蓝光影视的资源站](https://4kya.com/index.php/vod/show/by/time/id/1/page/22.html)
	# [最新连续剧 - 推荐连续剧 - 4K 鸭奈飞资源站 - 一个专做奈飞蓝光影视的资源站](https://4kya.com/index.php/vod/show/by/time/id/2/page/13.html)
	# [最新综艺 - 推荐综艺 - 4K 鸭奈飞资源站 - 一个专做奈飞蓝光影视的资源站](https://4kya.com/index.php/vod/show/by/time/id/3.html)
	# [最新动漫 - 推荐动漫 - 4K 鸭奈飞资源站 - 一个专做奈飞蓝光影视的资源站](https://4kya.com/index.php/vod/show/by/time/id/4.html)
	*[f'https://4kya.com/index.php/vod/show/by/time/id/{_type}/page/{i}.html'
	for _type, n in [(1, 22), (2, 13), (3, 1), (4, 1)]
	for i in range(n + 1)],
]
start_urls_v5 = [
	# 2021 02 23
	# sonic 数据过多检索异常, 重新爬取
	# 某网站如果页数过多, 所有分类的页数都/10
	# 超清
	# *[f'https://www.mdoutv.com/movie_bt/page/{i}' for i in range(1, 188)],
	*[f'https://www.wanmeikk.me/category/{_type}-{pageNo}.html'
	  for _type, n in [(1, 30), (2, 10), (3, 3), (4, 3), (5, 12), (6, 8), (7, 1), (8, 1), (9, 1), (10, 1)]
	  for pageNo in range(n + 1)],
	*[f'https://www.jpysvip.net/vodtype/{_type}-{i}.html'
	  for _type, n in [(1, 67), (2, 21), (3, 30), (4, 10)]
	  for i in range(n + 1)],
	*[f'https://hanmiys.com/vodtype/{_type}-{i}.html'
	  for _type, n in [(1, 76), (2, 33), (3, 77), (4, 18)]
	  for i in range(n + 1)],
	*[f'https://www.zhenbuka.com/vodtype/{_type}-{i}.html'
	  for _type, n in [(1, 77), (2, 36), (3, 20), (4, 10)]
	  for i in range(n + 1)],
	# 动漫
	*[f'http://agefans.org/catalog?page={i}' for i in range(1, 208)],
	*[f'http://www.bimiacg.com/type/{_type}-{i}/'
	  for _type, n in [('juchang', 15), ('fanzu', 65), ('guoman', 6), ('riman', 6)]
	  for i in range(n + 1)],
	*[f'http://www.dmdm2020.com/dongmantype/{_type}/page/{i}.html'
	  for _type, n in [(20, 31), (21, 3)]
	  for i in range(n + 1)],
	*[f'http://www.yhdm.io/{_type}/{i}.html'
	  for _type, n in [('japan', 50), ('china', 22), ('american', 7), ('movie', 12)]
	  for i in range(n + 1)],
	*[f'http://www.yxdm.me/resource/15-{i}.html' for i in range(1, 60)],
	# 2021 02 19
	# 动漫
	*[f'https://www.agefans.net/update?page={i}' for i in range(1, 60)],
	# [ZzzFun 动漫视频网 - (￣﹃￣)~zZZ - 最新日本动漫 - 推荐日本动漫 - 第 65 页](http://www.zzzfun.com/vod_type_id_1_page_65.html)
	# [ZzzFun 动漫视频网 - (￣﹃￣)~zZZ - 最新当季新番 - 推荐当季新番 - 第 7 页](http://www.zzzfun.com/vod_type_id_42_page_7.html)
	# [ZzzFun动漫视频网 - (￣﹃￣)~zZZ-最新剧场版OVA-推荐剧场版OVA-第14页](http://www.zzzfun.com/vod_type_id_3_page_14.html)
	*[f'http://www.zzzfun.com/vod_type_id_{_type}_page_{i}.html'
	  for _type, n in [(1, 65), (3, 14), (42, 7)]
	  for i in range(n + 1)],
	# 2021 02 22
	# 超清
	# [1080 影视 - 超清电影 - 1080 影视 - 电影电视剧免费看](https://www.ak1080.com/vodtype/1-877.html)
	# [1080 影视 - 超清电影 - 1080 影视 - 电影电视剧免费看](https://www.ak1080.com/vodtype/2-412.html)
	# [1080 影视 - 超清电影 - 1080 影视 - 电影电视剧免费看](https://www.ak1080.com/vodtype/3-36.html)
	# [1080 影视 - 超清电影 - 1080 影视 - 电影电视剧免费看](https://www.ak1080.com/vodtype/4-109.html)
	*[f'https://www.ak1080.com/vodtype/{_type}-{i}.html'
	  for _type, n in [(1, 87), (2, 41), (3, 3), (42, 10)]
	  for i in range(n + 1)],
	# [【日本动漫】- 奇奇动漫 第 532 页](https://www.qiqidongman.com/vod-search-order-vod_addtime-area-%E6%97%A5%E6%9C%AC-p-532.html)
	# [【国产动漫】- 奇奇动漫 第 149 页](https://www.qiqidongman.com/vod-search-order-vod_addtime-area-%E5%9B%BD%E4%BA%A7-p-149.html)
	*[f'https://www.qiqidongman.com/vod-search-order-vod_addtime-area-{_type}-p-{i}.html'
		for _type, n in [('%E6%97%A5%E6%9C%AC', 53), ('%E5%9B%BD%E4%BA%A7', 14)]
		for i in range(n + 1)],
	# [最新连载 - 推荐连载 - 新时空动漫](https://www.xskdm.com/vodshow/1--------3---.html)
	# [最新动漫电影 - 新时空动漫](https://www.xskdm.com/vodtype/2-2.html)
	# [完结动漫 - 新时空动漫](https://www.xskdm.com/vodtype/3-7.html)
	*[f'https://www.xskdm.com/vodtype/{_type}-{i}.html'
	  for _type, n in [(2, 2), (3, 7)]
	  for i in range(n + 1)],
	*[f'https://www.xskdm.com/vodtype/1--------{i}---.html' for i in range(1, 3+1)],
	# 2021 02 22
	# 4k
	# [最新电影 - 推荐电影 - 4K 鸭奈飞资源站 - 一个专做奈飞蓝光影视的资源站](https://4kya.com/index.php/vod/show/by/time/id/1/page/22.html)
	# [最新连续剧 - 推荐连续剧 - 4K 鸭奈飞资源站 - 一个专做奈飞蓝光影视的资源站](https://4kya.com/index.php/vod/show/by/time/id/2/page/13.html)
	# [最新综艺 - 推荐综艺 - 4K 鸭奈飞资源站 - 一个专做奈飞蓝光影视的资源站](https://4kya.com/index.php/vod/show/by/time/id/3.html)
	# [最新动漫 - 推荐动漫 - 4K 鸭奈飞资源站 - 一个专做奈飞蓝光影视的资源站](https://4kya.com/index.php/vod/show/by/time/id/4.html)
	*[f'https://4kya.com/index.php/vod/show/by/time/id/{_type}/page/{i}.html'
	for _type, n in [(1, 22), (2, 13), (3, 1), (4, 1)]
	for i in range(n + 1)],
]



# 低质量
# 'https://www.bttwo.com/new-movie/page/1',
# 'https://ddrk.me/page/1',
# *[f'https://www.itsck.com/type/{i}.html' for i in ['dianying', 'lianxuju', 'zongyi', 'dongman']],
# *[f'https://www.zhenbuka.com/vodtype/{i}' for i in range(1, 5)],
# *[f'https://www.tcmove.com/list/{i}.html' for i in ["dianying", 'lianxuju', 'zongyi', 'dongman']],
# *[f'https://kkmovie.cf/index.php/vod/type/id/{i}/page/1.html' for i in range(1, 5)],
# 'https://miao101.com/page/1',
# *[f'https://www.kpkuang.com/vodshow/{i}-------------.html' for i in range(1, 5)],
# *[f'http://www.bubulai.com/zv/{i}.html' for i in [10, 11]],
# *[f'https://www.novipnoad.com/tv/{i}/' for i in
#   ['hongkong', 'taiwan', 'western', 'japan', 'korea',
#    'other', 'anime', 'shows', 'life', 'movie']],



# *[f'http://www.bimibimi.me/type/juchang-{i}/' for i in range(2, 13 + 1)],
# *[f'http://www.bimibimi.me/type/fanzu-{i}/' for i in range(2, 55 + 1)],
# *[f'http://www.bimibimi.me/type/guoman-{i}/' for i in range(2, 4 + 1)],
# *[f'http://www.bimibimi.me/type/riman-{i}/' for i in range(2, 4 + 1)],
# *[f'https://www.novipnoad.com/tv/hongkong/page/{i}/' for i in range(2, 4 + 1)],
# *[f'https://www.novipnoad.com/tv/western/page/{i}/' for i in range(2, 93 + 1)],
# *[f'https://www.novipnoad.com/tv/japan/page/{i}/' for i in range(2, 418 + 1)],
# *[f'https://www.novipnoad.com/tv/korea/page/{i}/' for i in range(2, 119 + 1)],
# *[f'https://www.novipnoad.com/anime/page/{i}/' for i in range(2, 15 + 1)],
# *[f'https://www.novipnoad.com/shows/page/{i}/' for i in range(2, 3 + 1)],
# *[f'https://www.novipnoad.com/life/page/{i}/' for i in range(2, 2 + 1)],
# *[f'https://www.novipnoad.com/movie/page/{i}/' for i in range(2, 63 + 1)],
# * [f'http://www.bubulai.com/zv/10_{i}.html' for i in range(2, 92 + 1)],
# *[f'http://www.bubulai.com/zv/11_{i}.html' for i in range(2, 102 + 1)],
# *[f'http://www.66zhibo.net/{i}/' for i in [1, 2]],
# *[f'https://www.juqingba.cn/dianshiju/list_25_{i}.html' for i in range(1, 338 + 1)],
# *[f'http://agefans.org/catalog?page={i}' for i in range(136 + 1)],
# *[f'https://www.kpkuang.com/vodshow/1--------{i}-----.html' for i in range(1, 2581 + 1)],
# *[f'https://www.kpkuang.com/vodshow/2--------{i}-----.html' for i in range(1, 618 + 1)],
# *[f'https://www.kpkuang.com/vodshow/3--------{i}-----.html' for i in range(1, 155 + 1)],
# *[f'https://www.kpkuang.com/vodshow/4--------{i}-----.html' for i in range(1, 316 + 1)],
# *[f'https://miao101.com/page/{i}' for i in range(1, 2290 + 1)],
# *[f'https://kkmovie.cf/index.php/vod/type/id/1/page/{i}.html' for i in range(1, 3947 + 1)],
# *[f'https://kkmovie.cf/index.php/vod/type/id/2/page/{i}.html' for i in range(1, 1826 + 1)],
# *[f'https://kkmovie.cf/index.php/vod/type/id/3/page/{i}.html' for i in range(1, 320 + 1)],
# *[f'https://kkmovie.cf/index.php/vod/type/id/4/page/{i}.html' for i in range(1, 853 + 1)],
# *[f'http://www.zzzfun.com/vod-type-id-1-page-{i}.html' for i in range(1, 61 + 1)],
# *[f'http://www.zzzfun.com/vod-type-id-3-page-{i}.html' for i in range(1, 12 + 1)],
# *[f'http://www.qimiqimi.co/type/xinfan/page/{i}.html' for i in range(1, 6 + 1)],
# *[f'http://www.qimiqimi.co/type/riman/page/{i}.html' for i in range(1, 28 + 1)],
# *[f'http://www.qimiqimi.co/type/guoman/page/{i}.html' for i in range(1, 6 + 1)],
# *[f'http://www.qimiqimi.co/type/jcdm/page/{i}.html' for i in range(1, 8 + 1)],
# *[f'http://www.yxdm.me/resource/15-{i}.html' for i in range(1, 129 + 1)],
# *[f'http://www.yhdm.tv/japan/{i}.html' for i in range(2, 105 + 1)],
# *[f'http://www.yhdm.tv/china/{i}.html' for i in range(2, 21 + 1)],
# *[f'http://www.yhdm.tv/american/{i}.html' for i in range(2, 7 + 1)],
# *[f'http://www.yhdm.tv/movie/{i}.html' for i in range(2, 12 + 1)],
# *[f'https://www.tcmove.com/list/dianying-{i}.html' for i in range(1, 592)],
# *[f'https://www.tcmove.com/list/lianxuju-{i}.html' for i in range(1, 193)],
# *[f'https://www.tcmove.com/list/zongyi-{i}.html' for i in range(1, 158)],
# *[f'https://www.tcmove.com/show/dongman--------{i}---.html' for i in range(1, 198)],
# *[f'https://www.meijumi.net/usa/page/{i}/' for i in range(1, 218)],
# *[f'https://www.meijutt.tv/{i}_______.html' for i in range(1, 326)],
# *[f'https://www.wanmeikk.me/category/1-{i}.html' for i in range(1, 26)],
# *[f'https://www.wanmeikk.me/category/2-{i}.html' for i in range(1, 8)],
# *[f'https://www.wanmeikk.me/category/3-{i}.html' for i in range(1, 3)],
# *[f'https://www.wanmeikk.me/category/4-{i}.html' for i in range(1, 3)],