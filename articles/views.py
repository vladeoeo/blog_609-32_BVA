from django.shortcuts import render
from articles.models import Article

def article_list(request):
    articles= Article.objects.all().order_by('date')
    return render(request,"articles/article_list.html",{'articles':articles})

def article_item(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request,"articles/article_item.html",{"article":article})