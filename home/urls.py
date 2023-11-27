from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns =[
    path('',views.home, name='homepageHome'),
    path('contact/',views.contact, name='contactpageHome'),
    path('about/',views.about, name='aboutpageHome'),
    path('search', views.search, name='search'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.bloglogout, name='logout'),
    
]