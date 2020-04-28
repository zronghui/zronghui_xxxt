import math
from pprint import pprint

from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from utils import es, douban


def index(request):
    return render(request, 'index.html')


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
