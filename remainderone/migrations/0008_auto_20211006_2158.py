# Generated by Django 3.2.7 on 2021-10-06 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remainderone', '0007_follower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='message_date',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message_sent',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message_time',
        ),
        migrations.RemoveField(
            model_name='message',
            name='room_name',
        ),
    ]
