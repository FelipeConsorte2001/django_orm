# Generated by Django 4.0.2 on 2022-02-07 17:42

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_carro_motoristas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='montadora',
            field=models.ForeignKey(on_delete=models.SET(core.models.set_default_montadora), to='core.montadora'),
        ),
    ]
