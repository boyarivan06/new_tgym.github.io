from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model
from django.db.models import Model, CASCADE
from django.db.models import CharField, IntegerField, TextField, DateTimeField, ImageField, DateField
from django.db.models import OneToOneField, ForeignKey
from django.utils import timezone


class Blog(Model):
    author = ForeignKey(to=User, on_delete=CASCADE)
    datetime_created = DateTimeField(default=timezone.now)
    title = CharField(max_length=255, default='Новый блог')


class Post(Model):
    author = ForeignKey(to=User, on_delete=CASCADE)
    blog_id = ForeignKey(to=Blog, on_delete=CASCADE)
    datetime_created = DateTimeField(default=timezone.now)
    title = CharField(max_length=255, default='Новый пост')
    text = TextField(default='Текст блога')


class PhotoAlbum(Model):
    title = CharField(max_length=255, default='Новый фотоальбом')
    comment = TextField(default='Комментарий')
    image = ImageField(upload_to='images/')
    creator = ForeignKey(to=User, on_delete=CASCADE)


class Photo(Model):
    label = CharField(max_length=255)
    photoalbum = ForeignKey(to=PhotoAlbum, on_delete=CASCADE)
    image = ImageField(upload_to='images/')


class Grade(Model):
    year_grad = DateField()
    image = ImageField(upload_to='images/')
    blog = OneToOneField(to=Blog, on_delete=CASCADE)
    #  monitor = Teacher !!!
