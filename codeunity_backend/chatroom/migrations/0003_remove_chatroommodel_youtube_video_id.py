# Generated by Django 4.1.3 on 2022-11-24 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0002_rename_room_id_chatroommodel_room_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroommodel',
            name='youtube_video_id',
        ),
    ]
