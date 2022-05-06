# Generated by Django 4.0.4 on 2022-05-05 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCheckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('braintree_id', models.CharField(blank=True, max_length=120, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120)),
                ('street', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('zipcode', models.CharField(max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.usercheckout')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded')], default='created', max_length=120)),
                ('shipping_total_price', models.DecimalField(decimal_places=2, default=5.99, max_digits=50)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=50)),
                ('order_id', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to='orders.useraddress')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.cart')),
                ('shipping_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to='orders.useraddress')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.usercheckout')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
