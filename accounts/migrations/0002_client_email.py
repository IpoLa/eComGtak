# Generated by Django 3.2.13 on 2022-05-06 18:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default=datetime.datetime(2022, 5, 6, 18, 49, 27, 611314, tzinfo=utc), max_length=60, unique=True, verbose_name='email'),
            preserve_default=False,
        ),
    ]
