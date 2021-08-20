from django.db import models

# Create your models here.

class Stuff(models.Model):
    name = models.CharField(max_length=40, verbose_name="Ad və Soyad:")
    job = models.CharField(max_length=50, verbose_name="Peşə:")
    image = models.ImageField()


    class Meta:
        verbose_name = "İşçi"
        verbose_name_plural = "İşçilər"

    def __str__(self):
        return self.name
    
    