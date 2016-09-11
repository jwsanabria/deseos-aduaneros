# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deseo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deseo', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='deseo',
            name='personaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DeseosAduaneros.Personaje'),
        ),
    ]