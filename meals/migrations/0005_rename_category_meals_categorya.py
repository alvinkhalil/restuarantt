# Generated by Django 3.2.5 on 2021-08-08 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_meals_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meals',
            old_name='category',
            new_name='categorya',
        ),
    ]
