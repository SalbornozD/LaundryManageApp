from django.db import models

class Order(models.Model):
    client_name = models.CharField(max_length=100, default=None, blank=True, null=True)
    client_email = models.EmailField()
    receipt_date_time = models.DateTimeField(default=None, blank=True, null=True)
    delivery_date_time = models.DateTimeField(default=None, blank=True, null=True)

class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    detail = models.TextField()

class ImageItemOrder(models.Model):
    item_order = models.ForeignKey(ItemOrder, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='itemsOrders/')
