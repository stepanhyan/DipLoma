# Generated by Django 4.2.5 on 2023-11-17 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=28, verbose_name='Username')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Composition name')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, default='', upload_to='images/')),
                ('audio', models.FileField(default='', upload_to='audio/')),
                ('comments_users', models.ManyToManyField(related_name='commented_songs', through='compositions.Comment', to='compositions.userprofile')),
                ('likes_users', models.ManyToManyField(related_name='liked_songs', to='compositions.userprofile')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compositions.songs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compositions.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compositions.songs'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compositions.userprofile'),
        ),
    ]
