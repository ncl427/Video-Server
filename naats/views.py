from django.shortcuts import render
from django.http import HttpResponse
from naats.models import *

# Create your views here.
def index(request):

    '''
    # video-qualities
    quality1 = vidQualities(
        quality="HIGH"
    )
    quality1.save()
    quality2 = vidQualities(
        quality="MED"
    )
    quality2.save()
    quality3 = vidQualities(
        quality="LOW"
    )
    quality3.save()

    # video-types
    type1 = vidTypes(
        type="VIDEO"
    )
    type1.save()
    type2 = vidTypes(
        type="MP4"
    )
    type2.save()

    # naats
    naat1 = naats(
        name="Duniya ke ae Musafir",
        vidPath='~/content/videos/Duniya ke ae Musafir.mp4',
        imgPath='~/content/images/Duniya ke ae Musafir.jpg',
        xDimension=1064,
        yDimension=720,

        quality=1,
        type=1,
    )
    naat1.save()
    '''

    return HttpResponse("<h1>This is the Naats app homepage</h1>")