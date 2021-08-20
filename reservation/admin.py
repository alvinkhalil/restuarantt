from django.contrib import admin
from django.db import models

from .models import Reservation
# Register your models here.


class Reserv(admin.ModelAdmin):

    list_display = ["name","date","time","people"]
    list_filter = ["date"]

admin.site.register(Reservation,Reserv)
