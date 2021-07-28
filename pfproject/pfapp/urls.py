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
    path('createsong', pfapp.views.createsong, name="createsong"),
    path('deletesong/<str:id>', pfapp.views.deletesong, name="deletesong"),
    path('editsong/<str:id>', pfapp.views.editsong, name="editsong"),
    path('updatesong/<str:id>', pfapp.views.updatesong, name="updatesong"),
    path('add', pfapp.views.newphoto, name="add"),
    path('createphoto', pfapp.views.createphoto, name="createphoto"),
    path('deletephoto/<str:id>', pfapp.views.deletephoto, name="deletephoto"),
    path('editphoto/<str:id>', pfapp.views.editphoto, name="editphoto"),
    path('updatephoto/<str:id>', pfapp.views.updatephoto, name="updatephoto"),
] 