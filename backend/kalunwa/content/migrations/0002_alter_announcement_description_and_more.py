# Generated by Django 4.0.3 on 2022-03-12 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='description',
            field=models.CharField(default=' ', max_length=225),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
