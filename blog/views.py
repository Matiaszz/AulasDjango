from django.shortcuts import render


def blog(request):
    return render(request, 'blog/index.html')


def articles(request):
    return render(request, 'blog/articles.html')
