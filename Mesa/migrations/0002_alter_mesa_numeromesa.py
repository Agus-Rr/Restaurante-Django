# Generated by Django 4.2 on 2023-10-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mesa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='numeroMesa',
            field=models.IntegerField(),
        ),
    ]
