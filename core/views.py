from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from sorl.thumbnail import get_thumbnail
import os
import random


# Create your views here.
def index(request):
    return HttpResponse("index")


def thumbnail(request, size):
    files = os.listdir(settings.MEDIA_ROOT)
    if len(files) < 1 or ('cache' in files and len(files) == 1):
        raise Http404("brak zdjec w folderze")
    picture = random.choice(files)
    im = get_thumbnail(picture, size, crop='center', quality=99)
    try:
        readed_image = im.read()
    except IOError:
        raise Http404("blad dostepu do pliku")
    except Exception:
        raise Http404("nieokreslony blad")
    return HttpResponse(readed_image, content_type="image/jpeg")