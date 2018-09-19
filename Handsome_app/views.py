#_*_coding:utf8_*_
from django.shortcuts import HttpResponse,render
from datetime import datetime


def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })
#def index(request):
#    return HttpResponse("你好")
def index(request):
    return render(request, 'index.html')

