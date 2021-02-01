from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    text = "This is my first django project in Yektanet!"
    return HttpResponse(text)
