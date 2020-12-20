import math

from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from utils import sonic, douban, redis_utils


def index(request):
    return render(request, 'index.html')


def search_sort(i):
    # 值越大，越靠前
    m = {
        # 超清快速
        'www.wanmeikk.me': 9.1,
        'www.mengmiandaxia.com': 9.2,
        'www.fenggoudy1.com': 9.3,
        'www.mdoutv.com': 9.4,
        'www.jpysvip.net': 9.5,
        'hanmiys.com': 9.5,

        # 美剧
        'www.meijumi.net': 5,
        'www.meijutt.tv': 5,
        # 直播
        'www.66zhibo.net': 4,
        # 剧情
        'www.juqingba.cn': 3,
        'www.yue365.com': 3.1,
        # 动漫
        'agefans.org': 2.2,
        'www.qimiqimi.co': 2.1,
        'www.yhdm.tv': 2,
        'www.duomimh.com': 2,
        'www.bimibimi.me': 2,
        # 高清
        'www.novipnoad.com': 1.3,
        'www.bubulai.com': 1.2,
        'kkmovie.cf': 1,
        'www.kpkuang.com': 1,
        'miao101.com': 1,
        # 广告(不给屏蔽的那种)
        'zhenbuka': -1,
        'nfmovies.com': -1,
    }
    for key, value in m.items():
        if key in i['book_url']:
            return value
    return 0


domainSiteNameMap = {
    'www.jpysvip.net': '极品影视 - 超清|快速',
    'hanmiys.com': '孤单影院 - 超清|快速',
    'www.mdoutv.com': '麦豆TV - 超清|快速',
    'www.wanmeikk.me': "完美看看 - 超清|快速",
    'www.mengmiandaxia.com': "蒙面大侠 - 超清|快速",
    'www.fenggoudy1.com': "疯狗电影 - 超清|快速",
    'www.bttwo.com': "两个BT",
    'ddrk.me': "低端影视",
    'dvdhd.me': "碟影世界",
    'www.itsck.com': "sck电影网",
    'www.zhenbuka.com': "真不卡影院 - 广告",
    'app.movie': "APP影院",
    'www.meijumi.net': "美剧迷 - 美剧",
    'www.meijutt.tv': "美剧天堂 - 美剧",
    'www.tcmove.com': "太初电影",
    'www.yhdm.tv': "樱花动漫 - 动漫",
    'www.zzzfun.com': "zzzfun动漫视频网",
    'www.qimiqimi.co': "奇米奇米 - 动漫",
    'www.yxdm.me': "怡萱动漫 - 动漫",
    'kkmovie.cf': "KK电影网 - 高清 多线路",
    'miao101.com': "旋风视频 - 高清",
    'www.kpkuang.com': "看片狂人 - 高清 多线路",
    'agefans.org': "AGE动漫 - 动漫",
    'www.juqingba.cn': "剧情吧 - 剧情",
    'www.yue365.com': "365 - 播放平台、播放时间表",
    'www.66zhibo.net': "66直播网 - 直播",
    'www.bubulai.com': "部部来 - 高清",
    'www.novipnoad.com': "no vip no ad - 高清",
    'www.bimibimi.me': "哔咪哔咪 - 动漫",
    'www.dmdm2020.com': "哆咪动漫 - 动漫",
}


def addSiteName(hits):
    for hit in hits:
        domain = hit['book_url'].split('/', 3)[2]
        siteName = domainSiteNameMap.get(domain)
        if siteName:
            hit['book_name'] = hit['book_name'] + ' - ' + siteName


def search(request):
    # /search?q=123&pageno=1
    pageNo = int(request.GET.get('pageno', 0))
    q = request.GET.get('q')
    search_type = request.GET.get('search_type', 'movies')
    if not q:
        return render(request, 'index.html')
    # 限定搜索词长度在 1~40 之间
    if not 1 < len(q) < 40 or search_type not in ['movies', 'books']:
        search_result = {
            'hits': {'total': 0, 'hits': []},
            'took': 0
        }
    else:
        # redis_search_words.search(q)
        urls = sonic.search(q, _from=20 * pageNo, doc_type=search_type)
        search_result = redis_utils.getMoviesByUrls(urls)
    addSiteName(search_result)
    search_result.sort(key=search_sort, reverse=True)
    # allPageNo = math.ceil(search_result['hits']['total'] / 20)

    parseSuccess = False
    if search_type == 'movies':
        movie_detail = douban.getMovieDetailByQuery(q)
        if movie_detail and "code" not in movie_detail:
            parseSuccess = True

    context = {
        'q': q,
        'hits': search_result,
        'pageNo': pageNo,
        # 'allPageNo': allPageNo,
        'previousPage': pageNo - 1,
        'nextPage': pageNo + 1,
        'isFirstPage': pageNo == 0,
        # 'isLastPage': pageNo == allPageNo - 1,
        # 'time': search_result['took'],
        # 'count': search_result['hits']['total'],
        'search_type': search_type,
        # todo: 改进月排行榜
        # 'hot_search_words': redis_search_words.get_hot_search_words(),
        # 豆瓣相关
        'parseSuccess': parseSuccess,
    }
    if parseSuccess:
        movie_title = movie_detail['title']
        movie_id = movie_detail['id']
        rating_average = movie_detail['rating']['average']
        year_genres = f'{movie_detail["year"]} ‧ {"/".join(movie_detail["genres"])}'
        movie_poster = movie_detail['images']['medium']  # small medium large
        summary = movie_detail["summary"]
        summary = summary[:145] + '...' if len(summary) > 145 else summary
        directors = '/'.join(i['name'] for i in movie_detail['directors'])
        casts = '/'.join(i['name'] for i in movie_detail['casts'])
        context.update({'movie_title': movie_title,
                        'movie_id': movie_id,
                        'rating_average': rating_average,
                        'year_genres': year_genres,
                        'movie_poster': movie_poster,
                        'summary': summary,
                        # 'summary_more': summary[145:],
                        'directors': directors,
                        'casts': casts,
                        })
    return render(request, 'result.html', context=context)


def error_404(request, exception):
    return render(request, 'error_404.html')


def error_500(request):
    return render(request, 'error_500.html')
