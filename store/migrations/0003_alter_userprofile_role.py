# Generated by Django 5.1.3 on 2024-11-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('клиент', 'клиент'), ('курьер', 'курьер'), ('владелец магазина', 'владелец магазина'), ('admin', 'admin')], default='клиент', max_length=32),
        ),
    ]
