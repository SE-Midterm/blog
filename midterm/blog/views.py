from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post


def home(request):
    return render(request, 'home.html')


def post(request):
    if request.method == 'POST':
        t = request.POST.get('title')
        c = request.POST.get('content')
        add = Post(title=t, content=c)
        add.save()
        return redirect('home')
    return render(request, 'post.html')


def show(request, pk=0):
    return render(request, 'show.html')
