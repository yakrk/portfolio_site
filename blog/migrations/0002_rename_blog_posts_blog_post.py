# Generated by Django 4.1.7 on 2023-03-08 06:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blog_posts',
            new_name='Blog_post',
        ),
    ]
