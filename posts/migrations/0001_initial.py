# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 20:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('index', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=posts.models.empty_user, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Declaration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('content', models.TextField(default='')),
                ('views_count', models.BigIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=posts.models.empty_user, to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(on_delete=posts.models.empty_user, related_name='updated_declarations_fk', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='ImportantNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('content', models.TextField(default='')),
                ('views_count', models.BigIntegerField(default=0)),
                ('answers_count', models.IntegerField(default=0)),
                ('is_commentary', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=posts.models.empty_user, to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(on_delete=posts.models.empty_user, related_name='updated_notes_fk', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Важный пост',
                'verbose_name_plural': 'Важные посты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('content', models.TextField(default='')),
                ('views_count', models.BigIntegerField(default=0)),
                ('answers_count', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=posts.models.empty_user, to=settings.AUTH_USER_MODEL)),
                ('best_answer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='what_best_answer_fk', to='posts.Answer')),
                ('updater', models.ForeignKey(on_delete=posts.models.empty_user, related_name='updated_questions_fk', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=300)),
                ('url_name', models.CharField(default='', max_length=20)),
                ('messages_count', models.BigIntegerField(default=0)),
                ('topics_count', models.BigIntegerField(default=0)),
                ('has_parent', models.BooleanField(default=False)),
                ('has_child', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=posts.models.empty_user, related_name='created_sections_fk', to=settings.AUTH_USER_MODEL)),
                ('last_activity', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Question')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subsections_fk', to='posts.Section')),
                ('updater', models.ForeignKey(on_delete=posts.models.empty_user, related_name='updated_sections_fk', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Thank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_thanks_fk', to='posts.Answer')),
                ('from_user', models.ForeignKey(on_delete=posts.models.empty_user, related_name='from_user_thanks_fk', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_thanks_fk', to='posts.Question')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_thanks_fk', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Благодарность',
                'verbose_name_plural': 'Благодарности',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_fk', to='posts.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='updater',
            field=models.ForeignKey(on_delete=posts.models.empty_user, related_name='updated_answers_fk', to=settings.AUTH_USER_MODEL),
        ),
    ]
