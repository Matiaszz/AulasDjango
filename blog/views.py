from django.shortcuts import render


def blog(request):
    context = {
        'text': 'Pagina inicial do blog',
        'title': 'Allan - Blog'
    }
    return render(request, 'blog/index.html', context)


def articles(request):
    context = {
        'text': 'Artigos do blog',
        'title': 'Allan - Artigos'
    }

    return render(request, 'blog/articles.html', context)
