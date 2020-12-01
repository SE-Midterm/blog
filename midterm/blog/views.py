from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post


def home(request):
    posts = Post.objects.all()
    data = {
        'posts': posts,
    }

    return render(request, 'home.html', data)


def post(request):
    if request.method == 'POST':
        t = request.POST.get('title')
        c = request.POST.get('content')
        add = Post(title=t, content=c)
        add.save()
        return redirect('home')
    return render(request, 'post.html')


def show(request, pk=0):
    p = Post.objects.filter(id=pk)[0]
    data = {
        'post': p,
    }
    return render(request, 'show.html', data)
