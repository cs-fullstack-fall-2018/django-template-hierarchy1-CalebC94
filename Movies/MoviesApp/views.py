from django.shortcuts import render

from .models import Movies


def index(request):
    Movieslist= Movies.objects.all()
    context = {'Movieslist': Movieslist}
    return render(request, 'MoviesApp/index.html', context)

def about(request):
    return render(request, 'MoviesApp/about.html' )

def test(request):
    return render(request, 'MoviesApp/test.html' )