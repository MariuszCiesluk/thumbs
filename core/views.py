from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from sorl.thumbnail import get_thumbnail
import os
import re
import random


# Create your views here.
def index(request):
    return HttpResponse("index")

def check_size(size):
    """
    check is parameter 'size' has:
    * two digit values
    * 'x' beetween them
    """
    values = size.split('x')
    if len(values) < 2:
        raise Http404("brak dwoch wymiarow obrazka")
    first_number = values[0].isdigit()
    second_number = values[1].isdigit()
    if not first_number:
        raise Http404("pierwszy wymiar nie jest liczba")
    if not second_number:
        raise Http404("drugi wymiar nie jest liczba")

def thumbnail(request, size):
    """
    main function for getting image from folder, cropping
    and making response
    """
    files = os.listdir(settings.MEDIA_ROOT)
    check_size(size)
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