# Generated by Django 3.1.2 on 2021-06-15 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('position',), 'verbose_name': 'دستهبندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
    ]
