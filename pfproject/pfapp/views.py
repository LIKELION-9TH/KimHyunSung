from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def hobby(request):
    return render(request, "hobby.html")

def music(request):
    return render(request, "music.html")

def place(request):
    return render(request, "place.html")

def photo(request):
    return render(request, "photo.html")

def qna(request):
    return render(request, "qna.html")