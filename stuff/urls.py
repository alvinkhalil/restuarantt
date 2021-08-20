from stuff import views

from django.urls import path

app_name = "stuff"

urlpatterns = [

  path("",views.stuffs, name="stuff")
]
