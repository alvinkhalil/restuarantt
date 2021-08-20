from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(models.Model):


    name = models.CharField(max_length=50,verbose_name="Ad")
    slug = models.SlugField(blank=True, null=True)
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):

        return self.name

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"

class Meals(models.Model):

    category =ForeignKey(Category, on_delete=CASCADE,verbose_name="Kateqoriya")
    name = models.CharField(max_length=60,verbose_name="Ad")
    description = RichTextField(verbose_name="Haqqında")
    price= models.DecimalField(max_digits=5, decimal_places=2,verbose_name="Qiymət")
    people = models.IntegerField(verbose_name="Adam sayı")
    pre_time = models.IntegerField(verbose_name="Hazırlanma vaxtı")
    image = models.ImageField(upload_to = "meals",verbose_name="Şəkil")
    slug = models.SlugField(blank=True, null=True)

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Meals, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Məhsul"
        verbose_name_plural = "Məhsullar"

    def __str__(self):
        return self.name
