# Generated by Django 2.2 on 2020-02-20 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0013_transictions'),
    ]

    operations = [
        migrations.AddField(
            model_name='transictions',
            name='tprice',
            field=models.IntegerField(default=0),
        ),
    ]
