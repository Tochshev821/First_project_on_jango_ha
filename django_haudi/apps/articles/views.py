# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse('Hi world!')
#
# def test(request):
#     return HttpResponse(" da ya tak mogu")
from django.shortcuts import render
from django.http import HttpResponse

from django.http import Http404, HttpResponseRedirect
from .models import Article, Comment
from django.urls import reverse

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")

    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")
    return render(request, 'articles/detail.html', {'article': a})
    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect( reverse('articles:detail', args= (a.id,)))

def test(request):
    return HttpResponse("Hi world")
