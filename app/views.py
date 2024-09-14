from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime, os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории':  reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    """возвращает текущее время в формате Час:Миниты"""
    current_time = datetime.datetime.now().time().strftime("%H:%M")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    """возвращает список файлов в рабочей директории"""
    try:
        files = f'Cодержимое рабочей директории: {os.listdir(path='.')}'
        return HttpResponse(files)
    except OSError:
        raise NotImplemented
