# Generated by Django 4.1.7 on 2023-03-09 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='github_link',
            field=models.URLField(blank=True),
        ),
    ]
