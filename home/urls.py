from django.urls import path
from . import views

# request = solicitação do cliente para o servidor
# response = resposta do servidor para o cliente


urlpatterns = [
    path('', views.home),
]
