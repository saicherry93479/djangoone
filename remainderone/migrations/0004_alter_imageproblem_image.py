# Generated by Django 3.2.7 on 2021-10-06 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remainderone', '0003_imageproblem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageproblem',
            name='image',
            field=models.ImageField(upload_to='profile'),
        ),
    ]
