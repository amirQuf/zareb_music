# Generated by Django 3.1.2 on 2021-06-15 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20201120_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Musics', to='music.album'),
        ),
    ]
