# Generated by Django 3.2.5 on 2021-08-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('people', models.IntegerField()),
                ('pre_time', models.IntegerField()),
                ('image', models.ImageField(upload_to='meals')),
            ],
        ),
    ]
