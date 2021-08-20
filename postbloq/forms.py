from django import forms
from django.forms import widgets  
from .models import Comments

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = {"content","user","email"}

        widgets ={
            "content"         :widgets.Textarea(attrs={'class': 'form-control','placeholder':'Rəyinizi daxil edin','rows':'2'}),            "content"         :widgets.Textarea(attrs={'class': 'form-control','placeholder':'Rəyinizi daxil edin','rows':'2'}),
            "user"         :widgets.TextInput(attrs={'class': 'form-control','placeholder':'Adınızı daxil edin', 'type':'text'}),
            "email"         :widgets.EmailInput(attrs={'class': 'form-control','placeholder':'Elektron poçtunuzu daxil edin', 'type':'email'}),

        }

