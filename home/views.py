from django.shortcuts import render


def home(request):
    context = {
        # 'text': 'estamos na home',
        'title': 'Home',
    }
    return render(request, 'home/index.html', context)
