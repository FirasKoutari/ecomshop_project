# Generated by Django 4.1.3 on 2024-01-04 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PaymentApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderline',
            old_name='product_item',
            new_name='product',
        ),
    ]
