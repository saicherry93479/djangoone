# Generated by Django 3.2.7 on 2021-10-06 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remainderone', '0004_alter_imageproblem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]