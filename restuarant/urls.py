
from meals import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

from meals.views import gallery,menu,about,contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meals/',include("meals.urls", namespace="meals")),
    path('',views.index, name = "index"),
    path("reservation/",include("reservation.urls", namespace="reservation")),
    path("gallery/",gallery, name = "gallery"),
    path("menu/",menu, name = "menu"),
    path("postbloq/",include("postbloq.urls",namespace="postbloq")),
    path("about/",about, name = "about"),
    path("contact/",contact, name = "contact"),
    path("stuff/",include("stuff.urls",namespace="stuff")),




]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
