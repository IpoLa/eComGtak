# Generated by Django 3.2.13 on 2022-05-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=60, unique=True, verbose_name='email'),
        ),
    ]
