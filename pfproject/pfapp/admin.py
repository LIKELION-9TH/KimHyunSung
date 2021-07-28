from django.contrib import admin
from .models import Song
from .models import Photo

admin.site.register(Song)
admin.site.register(Photo)