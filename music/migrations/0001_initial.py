# Generated by Django 3.1.2 on 2020-11-20 15:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام البوم')),
                ('rapper', models.CharField(max_length=200, verbose_name='نام خواننده')),
                ('slug', models.SlugField(unique=True, verbose_name='ادرس')),
                ('cover', models.ImageField(upload_to='music-cover', verbose_name='کاور')),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'البوم',
                'verbose_name_plural': 'البوم ها',
                'ordering': ['publish_time'],
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام اهنگ')),
                ('rapper', models.CharField(max_length=200, verbose_name='نام خواننده')),
                ('mix_mastering', models.CharField(blank=True, max_length=200, null=True, verbose_name='موسیقی')),
                ('cover', models.ImageField(upload_to='music-cover', verbose_name='کاور')),
                ('cover_art', models.CharField(blank=True, max_length=100, null=True)),
                ('file', models.FileField(upload_to='music_file', verbose_name='فایل صوتی ')),
                ('slug', models.SlugField(unique=True, verbose_name='ادرس')),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('show', models.BooleanField(default=True, verbose_name='نمایش/عدم نمایش')),
                ('des', models.TextField(verbose_name='توضیحات')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.album')),
            ],
            options={
                'verbose_name': 'موسیقی',
                'verbose_name_plural': 'موسیقی ها',
                'ordering': ['publish_time'],
            },
        ),
    ]