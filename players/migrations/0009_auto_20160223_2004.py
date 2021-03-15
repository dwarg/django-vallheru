# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 19:04
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_player_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerrace',
            name='dexterity',
            field=models.DecimalField(decimal_places=3, default=Decimal('2'), max_digits=5),
        ),
        migrations.AddField(
            model_name='playerrace',
            name='endurance',
            field=models.DecimalField(decimal_places=3, default=Decimal('2'), max_digits=5),
        ),
        migrations.AddField(
            model_name='playerrace',
            name='hp',
            field=models.DecimalField(decimal_places=3, default=Decimal('2'), max_digits=5),
        ),
        migrations.AddField(
            model_name='playerrace',
            name='inteligence',
            field=models.DecimalField(decimal_places=3, default=Decimal('2'), max_digits=5),
        ),
        migrations.AddField(
            model_name='playerrace',
            name='max_dexterity',
            field=models.DecimalField(decimal_places=3, default=Decimal('40'), max_digits=5, max_length=60),
        ),
        migrations.AddField(
            model_name='playerrace',
            name='max_endurance',
            field=models.DecimalField(decimal_places=3, default=Decimal('40'), max_digits=5, max_length=60),
        ),
        migrations.AddField(
            model_name='playerrace',
            name='max_inteligence',
            field=models.DecimalField(decimal_places=3, default=Decimal('40'), max_digits=5, max_length=60),
        ),
        migrations.AddField(
            model_name='playerrace',
            name='max_speed',
            field=models.DecimalField(decimal_places=3, default=Decimal('40'), max_digits=5, max_length=60),
        ),
        migrations.AddField(
            model_name='playerrace',
            name='max_strength',
            field=models.DecimalField(decimal_places=3, default=Decimal('40'), max_digits=5, max_length=60),
        ),
        migrations.AddField(
            model_name='playerrace',
            name='max_willpower',
            field=models.DecimalField(decimal_places=3, default=Decimal('40'), max_digits=5, max_length=60),
        ),
        migrations.AddField(
            model_name='playerrace',
            name='speed',
            field=models.DecimalField(decimal_places=3, default=Decimal('2'), max_digits=5),
        ),
        migrations.AddField(
            model_name='playerrace',
            name='strength',
            field=models.DecimalField(decimal_places=3, default=Decimal('2'), max_digits=5),
        ),
        migrations.AddField(
            model_name='playerrace',
            name='willpower',
            field=models.DecimalField(decimal_places=3, default=Decimal('2'), max_digits=5),
        ),
    ]