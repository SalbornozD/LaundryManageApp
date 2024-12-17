# Generated by Django 5.1.4 on 2024-12-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management_module', '0002_order_status_alter_imageitemorder_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'Por retirar'), ('2', 'Retirado'), ('3', 'En progreso'), ('4', 'Por entregar'), ('5', 'Entregado')], default='C', max_length=1),
        ),
    ]