# Generated by Django 2.1.5 on 2019-05-02 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20190425_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
