from datetime import time
from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import CharField, DateTimeField, EmailField, TextField, TimeField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.shortcuts import redirect
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    title = CharField(max_length=100,verbose_name="Ad")
    content = RichTextField(max_length=5000,verbose_name="Mətin")
    author  = ForeignKey(User, null=True, on_delete=CASCADE,verbose_name="Yazıçı")
    created = DateTimeField(default=timezone.now)
    tags = TaggableManager(verbose_name="taqlar")
    category = ForeignKey("Category", null=True, on_delete=SET_NULL,verbose_name="Kateqoriya")
    image = models.ImageField(verbose_name="Şəkil")

    class Meta:
        verbose_name ="Postlar"
        verbose_name_plural = "Postlar"

    def __str__(self):
        return self.title

    
class Category(models.Model):
    
    name = CharField(max_length=50)

  
    class Meta:
        verbose_name = "Bloq Kateqoriya"
        verbose_name_plural = "Bloq Kateqoriyalar"

    def __str__(self):
        return self.name


class Comments(models.Model):

    user = CharField(max_length=50)
    post = ForeignKey(Post, on_delete=CASCADE)
    reply = ForeignKey("ReplyComments",on_delete=CASCADE, blank=True, null=True)
    content = TextField(max_length=500)
    created = DateTimeField(default = timezone.now)
    email = EmailField(max_length=100)


    def __str__(self):

        return self.content

    class Meta:
        verbose_name = "Rəy"
        verbose_name_plural = "Rəylər"

class ReplyComments(models.Model):
    
    user = CharField(max_length=50)
    post = ForeignKey(Post, on_delete=CASCADE)
    parent = ForeignKey("Comments",on_delete=CASCADE)
    content = TextField(max_length=500)
    created = DateTimeField(default = timezone.now)
    email = EmailField(max_length=100)

    
    def __str__(self):

        return self.content

    class Meta:
        verbose_name = "Cavab"
        verbose_name_plural = "Cavablar"