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
    path('new', pfapp.views.newmusic, name="new"),
    path('create', pfapp.views.createsong, name="create"),
    path('delete/<str:id>', pfapp.views.deletesong, name="delete"),
    path('edit/<str:id>', pfapp.views.editsong, name="edit"),
    path('update/<str:id>', pfapp.views.update, name="update"),
]