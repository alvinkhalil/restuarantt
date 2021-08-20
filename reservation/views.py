from django.shortcuts import redirect, render
from .forms import ReservationForm
from settings.models import Settings
from django.contrib import messages


# Create your views here.


def reservation(request):
    
    form = ReservationForm()
    settings = Settings.objects.all()

    if request.method == "POST":

        form = ReservationForm(request.POST)

        if form.is_valid():

            form.save()
            
            messages.success(request,"Rezerv üçün təşəkkürlər, sizinlə əlaqə saxlanılacaq.")
            return redirect("index")


    context = {"form":form,"settings":settings}
    return render(request,"Reservation/reservation.html",context)