# Generated by Django 4.2.5 on 2023-11-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compositions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='comments_users',
        ),
    ]