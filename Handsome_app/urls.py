#_*_coding:utf8_*_
from django.urls import path
from . import views
urlpatterns = [
    path('1', views.index, name='index'),
    path('2', views.hello_world, name='hello_world'),
]