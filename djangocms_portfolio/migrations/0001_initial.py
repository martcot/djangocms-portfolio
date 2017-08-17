# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields
import taggit.managers
import filer.fields.folder
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Catégories',
                'verbose_name': 'Catégorie',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('slug', models.SlugField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Publié le')),
                ('description', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Description de la réalisation')),
                ('client', models.CharField(null=True, max_length=255, verbose_name='Client', blank=True)),
                ('location', models.CharField(null=True, max_length=255, verbose_name='Lieu', blank=True)),
                ('category', models.ForeignKey(to='djangocms_portfolio.CategoryWork', verbose_name='Catégorie')),
                ('folder', filer.fields.folder.FilerFolderField(null=True, verbose_name='Dossier de la gallerie', blank=True, to='filer.Folder')),
                ('head_picture', filer.fields.image.FilerImageField(to='filer.Image', verbose_name='En-tête')),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.')),
            ],
            options={
                'verbose_name_plural': 'Réalisations',
                'verbose_name': 'Réalisation',
            },
        ),
    ]
