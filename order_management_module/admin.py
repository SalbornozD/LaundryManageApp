from django.contrib import admin
from .models import Order, ItemOrder, ImageItemOrder

admin.site.register(Order)
admin.site.register(ItemOrder)
admin.site.register(ImageItemOrder)

# Register your models here.
