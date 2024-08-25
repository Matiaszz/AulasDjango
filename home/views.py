from django.shortcuts import render


def home(request):
    context = {
        'text': 'estamos na home'
    }
    return render(request, 'home/index.html', context)
