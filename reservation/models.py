from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField, DateTimeField, EmailField, TextField
from django.shortcuts import render

# Create your models here.

class Reservation(models.Model):

    CHOICES = (
    ('1 nəfərlik', '1 nəfərlik'),
    ('2 nəfərlik', '2 nəfərlik'),
    ('3 nəfərlik', '3 nəfərlik'),
    ('4 nəfərlik', '4 nəfərlik'),
    ('5 nəfərlik', '5 nəfərlik'),
    ('6 nəfərlik', '6 nəfərlik'),
    ('7 nəfərlik', '7 nəfərlik'),
    ('8 nəfərlik', '8 nəfərlik'),
    )
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=120)
    number = models.IntegerField()
    people = models.TextField(choices = CHOICES)
    date = models.DateField() 
    time = models.TimeField()

    def __str__(self):

        return self.name


    class Meta:
        verbose_name = "Reservasiya"
        verbose_name_plural = "Rezervasiyalar"
