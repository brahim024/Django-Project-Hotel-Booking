# Generated by Django 2.2.2 on 2019-07-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0010_auto_20190723_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]