from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import redirect, render, get_object_or_404
from .models import Photo, Song

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

def newmusic(request):
    return render(request, 'newmusic.html')

def newphoto(request):
    return render(request, 'newphoto.html')

#노래 페이지
def createsong(request):
    new_song = Song()
    new_song.title = request.POST['title']
    new_song.singer = request.POST['singer']
    new_song.body = request.POST['body']
    new_song.save()
    return redirect('music')

def deletesong(request, id):
    delete_song = Song.objects.get(id=id)
    delete_song.delete()
    return redirect('music')

def editsong(request, id):
    edit_song = Song.objects.get(id=id)
    return render(request, 'editsong.html', {'song':edit_song})

def updatesong(request, id):
    update_song = Song.objects.get(id=id)
    update_song.title = request.POST['title']
    update_song.singer = request.POST['singer']
    update_song.body = request.POST['body']
    update_song.save()
    return redirect('music')

#사진페이지
def createphoto(request):
    new_photo = Photo()
    new_photo.title = request.POST['title']
    new_photo.image = request.FILES.get('image')
    new_photo.body = request.POST['body']
    new_photo.save()
    return redirect('photo')

def deletephoto(request, id):
    delete_photo = Photo.objects.get(id=id)
    delete_photo.delete()
    return redirect('photo')

def editphoto(request, id):
    edit_photo = Photo.objects.get(id=id)
    return render(request, 'editphoto.html', {'photo':edit_photo})

def updatephoto(request, id):
    update_photo = Photo.objects.get(id=id)
    update_photo.title = request.POST['title']
    update_photo.image = request.FILES.get('image')
    update_photo.body = request.POST['body']
    update_photo.save()
    return redirect('photo')