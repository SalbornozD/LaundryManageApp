from django.urls import path
from .views import create_order, view_order, edit_order, delete_orders

urlpatterns = [
    path("create/", create_order, name="create_order"),
    path('<int:order_id>/', view_order, name='order_detail'),
    path('edit/<int:order_id>/', edit_order, name='edit_order'),
    path('delete/<int:order_id>/', delete_orders, name='delete_order'),
]