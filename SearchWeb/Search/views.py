import math
from pprint import pprint

from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
import es


def index(request):
    return render(request, 'index.html')


def search(request):
    # https://lookao.com/search?q=123&pageno=1
    pageNo = int(request.GET.get('pageno', 0))
    q = request.GET.get('q')
    search_result = es.search(q, _from=10 * pageNo)
    allPageNo = math.ceil(search_result['hits']['total'] / 10)
    context = {
        'q': q,
        'hits': [{'book_url': i['_source']['book_url'],
                  'book_name': i['highlight']['book_name'][0],
                  'book_desc': i['_source'].get('book_desc')
                  } for i in search_result['hits']['hits']],
        'pageNo': pageNo,
        'allPageNo': allPageNo,
        'previousPage': pageNo-1,
        'nextPage': pageNo+1,
        'isFirstPage': pageNo == 0,
        'isLastPage': pageNo == allPageNo
    }
    pprint(context)
    return render(request, 'result.html', context=context)
