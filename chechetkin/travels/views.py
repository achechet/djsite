from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Страница приложения Travels")

def categories(request):
    return HttpResponse("<h2>Список статей по странам</h2>")
