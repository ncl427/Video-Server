from django.shortcuts import render
from django.http import HttpResponse
# from videos.models import *

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is the Videos app homepage</h1>")

def list(request):
    return render(request, 'list.html')

def detail(request, videoId, name):
    # name = 'KungFuPandaTrailer.mp4'
    return render(request, 'detail.html', {'videoId': videoId, 'name': name})

