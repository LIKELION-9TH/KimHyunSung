from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern
import pfapp.views

urlpatterns = [
    path('pfapp/', pfapp.views.home, name="portfolio"),
    path('pfapp/hobby', pfapp.views.hobby, name = "hobby" ),
    path('pfapp/photo', pfapp.views.photo, name = "photo" ),
    path('pfapp/place', pfapp.views.place, name = "place" ),
    path('pfapp/music', pfapp.views.music, name = "music" ),
    path('pfapp/qna', pfapp.views.qna, name = "qna" ),
]