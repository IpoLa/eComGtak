# Generated by Django 3.2.13 on 2022-05-18 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_slide'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='image',
            field=models.ImageField(blank=True, default='category/default.jpg', upload_to='slide'),
        ),
    ]
