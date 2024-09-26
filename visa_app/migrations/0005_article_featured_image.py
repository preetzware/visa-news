# Generated by Django 4.2.15 on 2024-09-26 13:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visa_app', '0004_article_dislikes_alter_article_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
