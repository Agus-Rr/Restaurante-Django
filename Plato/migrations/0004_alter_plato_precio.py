# Generated by Django 4.2 on 2023-12-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plato', '0003_alter_plato_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
