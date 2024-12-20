# Generated by Django 5.1.4 on 2024-12-12 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('client_email', models.EmailField(max_length=254)),
                ('receipt_date_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('delivery_date_time', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageItemOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/itemsOrders')),
                ('item_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_management_module.itemorder')),
            ],
        ),
        migrations.AddField(
            model_name='itemorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_management_module.order'),
        ),
    ]
