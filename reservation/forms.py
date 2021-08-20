from django import forms
from django.forms import widgets
from django.forms.widgets import DateInput, Select, TextInput, TimeInput
from .models import Reservation


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'



class ReservationForm(forms.ModelForm):
    date= forms.DateField(widget = DateInput)
    time = forms.TimeField(widget = TimeInput)
    class Meta:
        model = Reservation
        fields = "__all__"
        widgets = {
            "name"         : TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder':'Ad','required data-error':'Xahiş olunur adınızı daxil edin'}),
            "email"         : TextInput(attrs={'class': 'form-control','id': 'email', 'placeholder':'Email','required data-error':'Xahiş olunur elektron poçtunuzu daxil edin'}),
            "number"         : TextInput(attrs={'class': 'form-control','id': 'phone', 'placeholder':'Əlaqə Nömrəsi','required data-error':'Xahiş olunur əlaqə nömrənizi daxil edin'}),
            "date"         : DateInput(attrs={'class': 'datepicker picker__input form-control','name':'date','id':'input_date', 'type':'text', 'value':'', 'required data-error':'Xahiş olunur tarixi seçin'}),
            "time"         : TimeInput(attrs={'class': 'time form-control picker__input','id':'input_time', 'required data-error':'Xahiş olunur vaxtı seçin'}),
            "people"         :Select(attrs={'class': 'form-control', 'placeholder':'Adam sayı','required data-error':'Xahiş olunur adam sayını daxil edin'}),

            
        }
