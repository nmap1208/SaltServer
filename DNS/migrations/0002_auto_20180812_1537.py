# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-12 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DNS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dns',
            name='type',
            field=models.CharField(choices=[(b'A', b'A- \xe5\xb0\x86\xe5\x9f\x9f\xe5\x90\x8d\xe6\x8c\x87\xe5\x90\x91\xe4\xb8\x80\xe4\xb8\xaaIPV4\xe5\x9c\xb0\xe5\x9d\x80'), (b'CNAME', b'CNAME- \xe5\xb0\x86\xe5\x9f\x9f\xe5\x90\x8d\xe6\x8c\x87\xe5\x90\x91\xe5\x8f\xa6\xe5\xa4\x96\xe4\xb8\x80\xe4\xb8\xaa\xe5\x9f\x9f\xe5\x90\x8d'), (b'AAAA', b'AAAA- \xe5\xb0\x86\xe5\x9f\x9f\xe5\x90\x8d\xe6\x8c\x87\xe5\x90\x91\xe4\xb8\x80\xe4\xb8\xaaIPV6\xe5\x9c\xb0\xe5\x9d\x80')], default=b'A', max_length=128, verbose_name='\u8bb0\u5f55\u7c7b\u578b'),
        ),
    ]
