from django.shortcuts import render
from blog.data import posts


def blog(request):
    # aqui a gente define as "variaveis" do codigo django, por exemplo:
    # blog\index.html:
    #     {% block posts %}
    #     {% for post in posts %}
    #         {% include "global/partials/postBlock.html" %}
    #     {% endfor %}
    #     {% comment %} posts do link do blog {% endcomment %}
    #     {% endblock posts %}
    context = {
        'text': 'Pagina inicial do blog',
        'title': 'Allan - Blog',
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)


def articles(request):
    context = {
        'text': 'Artigos do blog',
        'title': 'Allan - Artigos'
    }

    return render(request, 'blog/articles.html', context)


def post(request, id):
    context = {
        'text': 'Posts',
        'title': 'Allan - Postagem',
        'post': posts
    }
    return render(request, 'blog/index.html', context)
