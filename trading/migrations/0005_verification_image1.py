# Generated by Django 2.2 on 2020-02-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0004_verification'),
    ]

    operations = [
        migrations.AddField(
            model_name='verification',
            name='image1',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]
