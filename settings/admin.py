from meals.views import contact
from django.contrib import admin
from .models import Settings,contactus
# Register your models here.

class SettingsAdmin(admin.ModelAdmin):

    list_display = ["title", "status"]

admin.site.register(Settings,SettingsAdmin)


admin.site.register(contactus)