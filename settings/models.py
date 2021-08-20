from django.db import models
from django.db.models.fields import CharField, DateTimeField, EmailField, IntegerField, TextField
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField


# Create your models here.

class Settings(models.Model):

    STATUS = (
        ('True', 'Bəli'),
        ('False','Xeyr'),
    )


    title = CharField(max_length=40, verbose_name="Başlıq")
    about_short = RichTextField(verbose_name = "Kiçik hekayə")
    about = RichTextField(verbose_name="Haqqında")
    phone = IntegerField(verbose_name="Telefon1")
    phone2 = IntegerField(verbose_name="Telefon2",blank=True, null=True)

    email = EmailField(max_length=100,verbose_name="Elektron Poçt")
    location = CharField(max_length=400, verbose_name="Məkan")
    worktime = CharField(max_length=100,verbose_name="İş vaxtları")
    contanctinf = CharField(max_length=200,verbose_name="Əlaqə Məlumatları",blank=True, null=True)
    facebook = CharField(max_length=400,verbose_name="Facebook link")
    instagram = CharField(max_length=400,verbose_name="Instagran link")
    twitter = CharField(max_length=400,verbose_name="Twitter link")
    google = CharField(max_length=400,verbose_name="Google link")
    google_map =CharField(max_length=10000,verbose_name="Xəritə link")
    icon = ImageField()
    status= models.CharField(max_length=10, choices=STATUS)
    created_at= DateTimeField(auto_now_add=True)
    updated_at= DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Parametr"
        verbose_name_plural = "Parametrlər"


class contactus(models.Model):

    name = CharField(max_length=100)
    email = EmailField(max_length=100)
    title =CharField(max_length=40)
    message = TextField(max_length=10000)
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return self.title

        
    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"
