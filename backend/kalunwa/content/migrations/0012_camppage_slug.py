# Generated by Django 4.0.3 on 2022-06-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_merge_20220509_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='camppage',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]