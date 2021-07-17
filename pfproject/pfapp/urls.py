from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern
import pfapp.views

urlpatterns = [
    path('', pfapp.views.home, name="home"),
    path('hobby', pfapp.views.hobby, name = "hobby" ),
    path('photo', pfapp.views.photo, name = "photo" ),
    path('place', pfapp.views.place, name = "place" ),
    path('music', pfapp.views.music, name = "music" ),
    path('qna', pfapp.views.qna, name = "qna" ),
    path('/new', pfapp.views.new, name="new"),
    path('create', pfapp.views.create, name="create"),
    path('delete/<str:id>', pfapp.views.delete, name="delete"),
]