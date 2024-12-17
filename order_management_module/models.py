from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('1', 'Por retirar'),
        ('2', 'Retirado'),
        ('3', 'En progreso'),
        ('4', 'Por entregar'),
        ('5', 'Entregado'),
    ]

    client_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    client_email = models.EmailField()
    receipt_date_time = models.DateTimeField(default=None, blank=True, null=True)
    delivery_date_time = models.DateTimeField(default=None, blank=True, null=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='3',
    )

class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    detail = models.TextField()

class ImageItemOrder(models.Model):
    item_order = models.ForeignKey(ItemOrder, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='itemsOrders/')
