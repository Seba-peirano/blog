# Generated by Django 4.1.3 on 2023-01-13 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagen',
        ),
    ]
