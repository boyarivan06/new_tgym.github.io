# Generated by Django 4.1.5 on 2023-01-27 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgym', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='Новый блог', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='Текст блога'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Новый пост', max_length=255),
        ),
    ]
