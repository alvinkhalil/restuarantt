from django.shortcuts import render
from .models import Stuff
from settings.models import Settings

# Create your views here.

def stuffs(requst):

    stuffs = Stuff.objects.all()
    settings = Settings.objects.all()

    context = {
        "stuffs":stuffs,
        "settings":settings
    }

    return render(requst,"Home/stuff.html",context)