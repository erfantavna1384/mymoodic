# Generated by Django 4.1.1 on 2022-10-30 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]