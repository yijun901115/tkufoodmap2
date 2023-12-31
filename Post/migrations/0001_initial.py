# Generated by Django 4.2.2 on 2023-07-24 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('brief', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('linkage', models.URLField(blank=True, max_length=140)),
                ('Cover', models.ImageField(blank=True, upload_to='media/postCoverPicture/')),
                ('image', models.ImageField(blank=True, upload_to='media/postPicture/')),
                ('video', models.FileField(blank=True, upload_to='media/postVideo/')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
