# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.folder
import taggit.managers
import filer.fields.image
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryWork',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Catégorie',
                'verbose_name_plural': 'Catégories',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('slug', models.SlugField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Published on')),
                ('description', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Work Description')),
                ('client', models.CharField(max_length=255, verbose_name='Client', blank=True, null=True)),
                ('location', models.CharField(max_length=255, verbose_name='Location', blank=True, null=True)),
                ('category', models.ForeignKey(to='portfolio.CategoryWork', verbose_name='Catégorie')),
                ('folder', filer.fields.folder.FilerFolderField(blank=True, to='filer.Folder', null=True, verbose_name='Gallery Folder')),
                ('head_picture', filer.fields.image.FilerImageField(to='filer.Image', verbose_name='Head')),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', through='taggit.TaggedItem', to='taggit.Tag', help_text='A comma-separated list of tags.')),
            ],
            options={
                'verbose_name': 'Work',
                'verbose_name_plural': 'Works',
            },
        ),
    ]
