# Generated by Django 3.0.5 on 2020-05-01 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibecheck', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='multi_media',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
