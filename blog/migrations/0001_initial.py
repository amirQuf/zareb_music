# Generated by Django 3.1.2 on 2020-11-21 15:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.BooleanField()),
                ('position', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('cover', models.ImageField(upload_to='blog-cover', verbose_name='عکس بندانگشتی')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('slug', models.SlugField(unique=True, verbose_name='ادرس')),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('p', 'انتشار'), ('d', 'پیش نویس')], max_length=1)),
                ('pin', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='blog.Category')),
            ],
            options={
                'verbose_name': 'وبلاگ',
                'verbose_name_plural': 'وبلاگ ها',
                'ordering': ['publish_time'],
            },
        ),
    ]