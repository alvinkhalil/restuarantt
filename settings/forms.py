from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import contactus


class ContactusForm(forms.ModelForm):

    class Meta:
        model = contactus

        fields = ["name","email","title","message"]
           
        widgets ={  
             "name"          :widgets.TextInput(attrs={'class': 'form-control', 'type':'text','placeholder':'Adınız','required data-error':'Xahiş olunur adınızı daxil edin'}),
             "email"         :widgets.EmailInput(attrs={'class': 'form-control', 'type':'text','placeholder':'Email','required data-error':'Xahiş olunur emailinizi daxil edin'}),
             "message"         :widgets.Textarea(attrs={'class': 'form-control', 'type':'text','placeholder':'Mesaj','required data-error':'Xahiş olunur mesajınızı daxil edin'}),
             "title"          :widgets.TextInput(attrs={'class': 'form-control', 'type':'text','placeholder':'Başlıq','required data-error':'Xahiş olunur başlıqı daxil edin'}),

        }

