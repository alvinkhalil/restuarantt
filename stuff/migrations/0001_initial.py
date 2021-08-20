# Generated by Django 3.2.5 on 2021-08-16 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Ad və Soyad:')),
                ('job', models.CharField(max_length=50, verbose_name='Peşə:')),
            ],
            options={
                'verbose_name': 'İşçi',
                'verbose_name_plural': 'İşçilər',
            },
        ),
    ]