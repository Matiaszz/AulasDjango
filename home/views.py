# from django.shortcuts import render
from django.http import HttpResponse


def home(request) -> HttpResponse:
    return HttpResponse('HOME APP')
