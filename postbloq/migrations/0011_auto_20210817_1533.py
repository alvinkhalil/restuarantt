# Generated by Django 3.2.5 on 2021-08-17 11:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('postbloq', '0010_comments_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=500)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postbloq.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postbloq.post')),
            ],
            options={
                'verbose_name': 'Cavab',
                'verbose_name_plural': 'Cavablar',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='postbloq.replycomments'),
        ),
    ]
