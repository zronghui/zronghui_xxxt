import math
from pprint import pprint

from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from utils import es, douban


def index(request):
    return render(request, 'index.html')


def search_sort(i):
    # 值越大，越靠前
    if 'www.juqingba.cn' in i['_source']['book_url']:
        return 4
    if 'agefans.org' in i['_source']['book_url']:
        return 3
    if 'www.qimiqimi.co' in i['_source']['book_url']:
        return 2
    if 'www.yhdm.tv' in i['_source']['book_url']:
        return 2
    if 'zhenbuka' in i['_source']['book_url']:
        return 1
    return 0


domainSiteNameMap = {
    'www.bttwo.com': "两个BT",
    'ddrk.me': "低端影视",
    'dvdhd.me': "碟影世界",
    'www.itsck.com': "sck电影网",
    'www.zhenbuka.com': "真不卡影院",
    'app.movie': "APP影院",
    'www.meijumi.net': "美剧迷",
    'www.meijutt.tv': "美剧天堂",
    'www.wanmeikk.me': "完美看看",
    'www.tcmove.com': "太初电影",
    'www.yhdm.tv': "樱花动漫",
    'www.zzzfun.com': "zzzfun动漫视频网",
    'www.qimiqimi.co': "奇米奇米",
    'www.yxdm.me': "怡萱动漫",
    'kkmovie.cf': "KK电影网",
    'miao101.com': "旋风视频",
    'www.kpkuang.com': "看片狂人",
    'agefans.org': "AGE动漫",
    'www.juqingba.cn': "剧情吧",
    # '': {
    #     'urlsXpath': "/@href",
    #     'namesXpath': "/text()"
    # },
}


def addSiteName(hits):
    for hit in hits:
        domain = hit['_source']['book_url'].split('/', 3)[2]
        siteName = domainSiteNameMap.get(domain)
        if siteName:
            hit['highlight']['book_name'][0] = hit['highlight']['book_name'][0] + ' - ' + siteName


def search(request):
    # https://lookao.com/search?q=123&pageno=1
    pageNo = int(request.GET.get('pageno', 0))
    q = request.GET.get('q')
    search_type = request.GET.get('search_type', 'movies')
    # 限定搜索词长度在 1~40 之间
    if not 1 < len(q) < 40 or search_type not in ['movies', 'books']:
        search_result = {
            'hits': {'total': 0, 'hits': []},
            'took': 0
        }
    else:
        search_result = es.search(q, _from=20 * pageNo, doc_type=search_type)
    addSiteName(search_result['hits']['hits'])
    search_result['hits']['hits'].sort(key=search_sort, reverse=True)
    allPageNo = math.ceil(search_result['hits']['total'] / 20)

    parseSuccess = False
    if search_type == 'movies':
        movie_detail = douban.getMovieDetailByQuery(q)
        if movie_detail and "code" not in movie_detail:
            parseSuccess = True

    context = {
        'q': q,
        'hits': [{'book_url': i['_source']['book_url'],
                  'book_name': i['highlight']['book_name'][0],
                  'book_desc': i['_source'].get('book_desc')
                  } for i in search_result['hits']['hits']],
        'pageNo': pageNo,
        'allPageNo': allPageNo,
        'previousPage': pageNo - 1,
        'nextPage': pageNo + 1,
        'isFirstPage': pageNo == 0,
        'isLastPage': pageNo == allPageNo - 1,
        'time': search_result['took'],
        'count': search_result['hits']['total'],
        'search_type': search_type,
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
    pprint(context)
    return render(request, 'result.html', context=context)


def error_404(request, exception):
    return render(request, 'error_404.html')


def error_500(request):
    return render(request, 'error_500.html')
