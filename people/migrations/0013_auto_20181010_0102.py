# Generated by Django 2.0.7 on 2018-10-09 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0012_auto_20181010_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.FileField(upload_to='Posts'),
        ),
    ]
