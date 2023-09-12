from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model
from django.db.models import Model, CASCADE
from django.db.models import CharField, IntegerField, TextField, DateTimeField, ImageField, DateField, FileField
from django.db.models import OneToOneField, ForeignKey
from django.utils import timezone


class Base_Methods:
    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.objects.filter(id=id).first()


class Blog(Model, Base_Methods):
    author = ForeignKey(to=User, on_delete=CASCADE)
    datetime_created = DateTimeField(default=timezone.now)
    title = CharField(max_length=255, default='Новый блог')


class Post(Model, Base_Methods):
    author = ForeignKey(to=User, on_delete=CASCADE)
    blog = ForeignKey(to=Blog, on_delete=CASCADE)
    datetime_created = DateTimeField(default=timezone.now)
    title = CharField(max_length=255, default='Новый пост')
    text = TextField(default='Текст блога')


class PhotoAlbum(Model, Base_Methods):
    title = CharField(max_length=255, default='Новый фотоальбом')
    comment = TextField(default='Комментарий')
    image = ImageField(upload_to='images/')
    creator = ForeignKey(to=User, on_delete=CASCADE)


class Photo(Model, Base_Methods):
    label = CharField(max_length=255)
    photoalbum = ForeignKey(to=PhotoAlbum, on_delete=CASCADE)
    image = ImageField(upload_to='images/')


class Teacher(Model, Base_Methods):
    user = OneToOneField(to=User, on_delete=CASCADE)
    image = ImageField(upload_to='images/')
    name = CharField(max_length=255)
    surname = CharField(max_length=255)


class Grade(Model, Base_Methods):
    year_grad = DateField()
    image = ImageField(upload_to='images/')
    blog = OneToOneField(to=Blog, on_delete=CASCADE)
    #  monitor = Teacher !!!


class Pupil(Model, Base_Methods):
    grade = ForeignKey(Grade, CASCADE)
    user = OneToOneField(to=User, on_delete=CASCADE)
    image = ImageField(upload_to='images/')
    name = CharField(max_length=255)
    surname = CharField(max_length=255)
    birthdate = DateField()


class Hw(Model, Base_Methods):
    date = DateField(default=timezone.now)
    text = TextField()
    grade = ForeignKey(to=Grade, on_delete=CASCADE)


class Sked(Model, Base_Methods):
    date = DateField(default=timezone.now)
    file = FileField(upload_to='skeds/')
    creator = ForeignKey(to=User, on_delete=CASCADE)


class Video(Model, Base_Methods):
    video_source = CharField(max_length=255)
    label = CharField(max_length=255)
    creator = ForeignKey(to=User, on_delete=CASCADE)
    datetime_created = DateTimeField(default=timezone.now)
