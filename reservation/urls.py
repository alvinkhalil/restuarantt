from meals import views


from reservation import views
from django.urls import path

app_name = "reservation"

urlpatterns = [

  path("",views.reservation, name="reserv")
]
