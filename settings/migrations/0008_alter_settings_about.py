# Generated by Django 3.2.5 on 2021-08-14 14:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_alter_settings_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='about',
            field=ckeditor.fields.RichTextField(verbose_name='Haqqında'),
        ),
    ]