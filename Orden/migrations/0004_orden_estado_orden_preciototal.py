# Generated by Django 4.2.4 on 2023-11-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orden', '0003_remove_orden_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orden',
            name='precioTotal',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]