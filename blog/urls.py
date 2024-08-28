from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<int:id>/', views.post, name='post'),
    path('articles/', views.articles, name='articles'),
]
