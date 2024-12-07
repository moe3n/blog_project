from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Articles
from django.http import HttpResponse


# Create your views here.
def article_list(request):
    articles = Articles.objects.all().order_by('date')

    return render(request,'articles/articles_list.html', {'articles':articles})

def article_detail(request, slug):
    articles = Articles.objects.all()
    article= get_object_or_404(articles, slug=slug)
    print("article is ",article)
    
    return render(request,'articles/article_detail.html', {'article':article})
