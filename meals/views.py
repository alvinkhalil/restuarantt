from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Meals, Category
from settings.models import Settings, contactus
from settings.forms import ContactusForm
from django.core.mail import send_mail, BadHeaderError
# Create your views here.




def meal_detail(request,slug):

    settings = Settings.objects.all()
    meals = Meals.objects.get(slug = slug)

    context = {

        "meals":meals,
        "settings":settings,

    }
    
    return render(request, "Meals/meals_detail.html",context)

def index(request):

    meals = Meals.objects.all()
    gallery = Meals.objects.all()[:6]
    categories = Category.objects.all()
    settings = Settings.objects.all()
    context = {
            "meals":meals,
            "categories":categories,
            "gallery":gallery,
            "settings":settings,
        }


    return render(request, "Home/index.html",context)

def about(request):
    settings = Settings.objects.all()
    context = {
    
            "settings":settings,
        }
    return render(request, "Home/about.html",context)


def contact(request):
    settings = Settings.objects.all()
    forms = ContactusForm()

    if request.method == "POST":

        forms = ContactusForm(request.POST)
        
        if forms.is_valid():
            forms.save()

            email = forms.cleaned_data['email']
            title = forms.cleaned_data['title']
            subject = forms.cleaned_data['message']

            try:
                send_mail(email,title,subject,['alvinkhalil@outlook.com'])
                messages.success(request, "Mesajınız uğurla göndərildi.")
                return redirect("index")

            except BadHeaderError:

                return HttpResponse("Səhv")
        
    context = {
    
            "settings":settings,
            "contacts":forms,
        }
    return render(request, "Home/contact.html",context)



def menu(request):

    meals = Meals.objects.all()
    categories = Category.objects.all()
    settings = Settings.objects.all()
    context = {
            "meals":meals,
            "categories":categories,
            "settings":settings,
        }

    return render(request, "Home/menu.html",context)


def gallery(request):

    gallery = Meals.objects.all()
    settings = Settings.objects.all()

    context = {
        "gallery":gallery,
        "settings":settings,
    }

    return render(request, "Home/gallery.html", context)

