# Generated by Django 4.0.3 on 2022-04-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_camppage_gallery_project_gallery_alter_event_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='jumbotron',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]