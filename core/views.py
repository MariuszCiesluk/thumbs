from django.shortcuts import render
from django.http import HttpResponse
from sorl.thumbnail import get_thumbnail


# Create your views here.
def index(request):
    return HttpResponse("index")


def thumbnail(request, size):
    return HttpResponse(size)