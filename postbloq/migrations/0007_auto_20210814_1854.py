# Generated by Django 3.2.5 on 2021-08-14 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postbloq', '0006_alter_post_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Bloq Kateqoriya', 'verbose_name_plural': 'Bloq Kateqoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Rəy', 'verbose_name_plural': 'Rəylər'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Postlar', 'verbose_name_plural': 'Postlar'},
        ),
    ]
