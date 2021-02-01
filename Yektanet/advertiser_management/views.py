from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import MakeAd
from .models import Advertiser, Ad


def index(request):
    text = "This is my first django project in Yektanet!"
    return HttpResponse(text)

