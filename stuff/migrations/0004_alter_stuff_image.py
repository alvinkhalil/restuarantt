# Generated by Django 3.2.5 on 2021-08-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0003_alter_stuff_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]