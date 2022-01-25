from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Travel.objects.all()
    return render(request, 'travels/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'travels/about.html', {'menu': menu,'title': 'О сайте'})

def categories(request, catid):
    return HttpResponse(f"<h2>Список статей по странам</h2><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')
