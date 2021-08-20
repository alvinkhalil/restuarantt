from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from meals import views

app_name = "meals"

urlpatterns = [
        path("<slug:slug>", views.meal_detail, name="meals_detail"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
