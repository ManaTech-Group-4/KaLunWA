# Generated by Django 4.0.3 on 2022-06-01 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0011_merge_20220509_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageContainedJumbotron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PageContainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=225, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('jumbotrons', models.ManyToManyField(through='page_containers.PageContainedJumbotron', to='content.jumbotron')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pagecontainedjumbotron',
            name='container',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_containers.pagecontainer'),
        ),
        migrations.AddField(
            model_name='pagecontainedjumbotron',
            name='jumbotron',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.jumbotron'),
        ),
        migrations.AddConstraint(
            model_name='pagecontainedjumbotron',
            constraint=models.UniqueConstraint(fields=('container', 'jumbotron', 'section_order'), name='unique_container_jumbo_order'),
        ),
        migrations.AddConstraint(
            model_name='pagecontainedjumbotron',
            constraint=models.UniqueConstraint(fields=('container', 'section_order'), name='unique_container_order'),
        ),
        migrations.AddConstraint(
            model_name='pagecontainedjumbotron',
            constraint=models.UniqueConstraint(fields=('container', 'jumbotron'), name='unique_container_jumbotron'),
        ),
    ]