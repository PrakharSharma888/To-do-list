from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.userlist, name='list'),
    path('add', views.addform, name='add'),
    path('delcomp', views.delcomp, name='delcomp'),
    path('delall', views.delall, name='delall'),
    path('comp/<item_id>', views.compform, name='comp'),
]
