# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 20:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='updater',
            field=models.ForeignKey(blank=True, null=True, on_delete=posts.models.empty_user, related_name='updated_questions_fk', to=settings.AUTH_USER_MODEL),
        ),
    ]
