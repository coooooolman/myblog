from django.shortcuts import render
from django.http import HttpResponse
from . import models


article=models.Article.objects.get(pk=1)
def index(request):
    return render(request, 'blog/index.html',{'article': article})