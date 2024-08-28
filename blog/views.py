from django.shortcuts import render
from django.http import HttpRequest, Http404
from blog.data import posts
from typing import Any


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


def post(request: HttpRequest, postID: int):

    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == postID:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe')

    context = {
        'text': 'Posts',
        'title': f'{found_post['title']}',
        'post': found_post
    }

    return render(request, 'blog/posts.html', context)
