# from django.shortcuts import render
from django.http import HttpResponse


def blog(request) -> HttpResponse:
    return HttpResponse('BLOG APP')
