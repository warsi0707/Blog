from django.contrib import admin
from django.urls import path,include
from myblog import views



urlpatterns =[
    path("", views.blogpage, name='blogpage'),
    path("<str:slug>", views.blogPost, name='blogPost'),
]