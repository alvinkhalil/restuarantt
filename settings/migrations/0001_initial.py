# Generated by Django 3.2.5 on 2021-08-14 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Başlıq')),
                ('about', models.TextField(max_length=10000, verbose_name='Haqqında')),
                ('phone', models.CharField(max_length=100, verbose_name='Telefon')),
                ('email', models.EmailField(max_length=100, verbose_name='Elektron Poçt')),
                ('location', models.CharField(max_length=400, verbose_name='Məkan')),
                ('worktime', models.CharField(max_length=100, verbose_name='İş vaxtları')),
                ('contanctinf', models.CharField(max_length=200, verbose_name='Əlaqə Məlumatları')),
                ('facebook', models.CharField(max_length=400, verbose_name='Facebook link')),
                ('instagram', models.CharField(max_length=400, verbose_name='Instagran link')),
                ('twitter', models.CharField(max_length=400, verbose_name='Twitter link')),
                ('google', models.CharField(max_length=400, verbose_name='Google link')),
                ('google_map', models.CharField(max_length=10000, verbose_name='Xəritə link')),
                ('icon', models.ImageField(upload_to='')),
                ('status', models.CharField(choices=[('True', 'Bəli'), ('False', 'Xeyr')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]