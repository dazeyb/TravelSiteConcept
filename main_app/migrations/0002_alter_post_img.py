# Generated by Django 3.2.3 on 2021-05-15 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.CharField(max_length=600),
        ),
    ]
