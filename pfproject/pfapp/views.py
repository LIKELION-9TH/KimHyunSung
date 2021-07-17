from django.shortcuts import redirect, render, get_object_or_404
from .models import Song

# Create your views here.
def home(request):
    return render(request, "home.html")

def hobby(request):
    return render(request, "hobby.html")

def music(request):
    songs = Song.objects.all()
    return render(request, "music.html", {'songs':songs})

def place(request):
    return render(request, "place.html")

def photo(request):
    return render(request, "photo.html")

def qna(request):
    return render(request, "qna.html")

def new(request):
    return render(request, 'new.html')

def create(request):
    new_song = Song()
    new_song.title = request.POST['title']
    new_song.singer = request.POST['singer']
    new_song.body = request.POST['body']
    new_song.save()
    return redirect('music')

def delete(request, id):
    delete_song = Song.objects.get(id=id)
    delete_song.delete()
    return redirect('music')