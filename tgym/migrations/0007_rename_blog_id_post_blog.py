# Generated by Django 4.1.5 on 2023-07-30 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgym', '0006_video_teacher_sked_pupil_hw'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='blog_id',
            new_name='blog',
        ),
    ]