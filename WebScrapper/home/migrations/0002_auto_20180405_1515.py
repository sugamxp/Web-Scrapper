# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResultFlipkart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameF', models.CharField(max_length=100)),
                ('priceF', models.CharField(max_length=264)),
                ('queryF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Search')),
            ],
        ),
        migrations.AlterField(
            model_name='searchresult',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
