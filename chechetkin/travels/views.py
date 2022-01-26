from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]

def index(request):
    posts = Travel.objects.all()
    context = {
        'posts': posts,
        'menu': menu, 
        'title': 'Главная страница'      
    }
    
    return render(request, 'travels/index.html', context=context)

def about(request):
    return render(request, 'travels/about.html', {'menu': menu,'title': 'О сайте'})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')
