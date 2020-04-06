from django.http import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def search(request):
    # https://lookao.com/search?q=123&pageno=1
    return render(request, 'result.html')
