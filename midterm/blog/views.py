from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def post(request):
    return render(request, 'post.html')


def show(request, pk=0):
    return render(request, 'show.html')
