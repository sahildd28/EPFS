from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home,name="mainp"),
    path('about/',views.about,name="about"),
    path('home/',views.button_click,name="btn_click"),
    path('home/',views.home,name="home"),
    path('base/',views.base,name="base")
]