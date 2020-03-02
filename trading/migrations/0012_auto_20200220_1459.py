# Generated by Django 3.0.3 on 2020-02-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0011_auto_20200214_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='statuses',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='user_signup',
            name='profileimg',
            field=models.ImageField(default='images/user.png', upload_to='images/'),
        ),
    ]