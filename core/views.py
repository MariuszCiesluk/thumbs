from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from sorl.thumbnail import get_thumbnail
import os
import random


# Create your views here.
def index(request):
    return HttpResponse("index")


def thumbnail(request, size):
    files = os.listdir(settings.MEDIA_ROOT)
    picture = random.choice(files)
    im = get_thumbnail(picture, size, crop='center', quality=99)
    return HttpResponseRedirect(im.url)