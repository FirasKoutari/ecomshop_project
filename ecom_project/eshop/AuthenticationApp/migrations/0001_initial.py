# Generated by Django 4.1 on 2023-11-26 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProductsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_value', models.IntegerField()),
                ('comment', models.TextField()),
                ('ordered_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductsApp.productitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AuthenticationApp.user')),
            ],
        ),
    ]
