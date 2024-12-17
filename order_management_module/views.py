from django.shortcuts import render, redirect
from .models import Order, ItemOrder, ImageItemOrder
from django.http import HttpResponse
from django.utils import timezone

def create_order(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_email = request.POST.get('client_email')

        order = Order.objects.create(
            client_name = client_name,
            client_email = client_email,
            receipt_date_time = timezone.now(),
        )

        item_keys = [key for key in request.POST if key.startswith('description_')]
        for key in item_keys:
            unique_id = key.split('_')[1]
            description = request.POST.get(f'description_{unique_id}')
            detail = request.POST.get(f'detail_{unique_id}')

            item_order = ItemOrder.objects.create(
                order = order,
                description = description,
                detail = detail
            )

            images = request.FILES.getlist(f'images_{unique_id}')
            for image in images:
                ImageItemOrder.objects.create(
                    item_order = item_order,
                    image = image
                )

        return redirect('home')
    
    return render(request, 'order_management_module/order-form.html', {})
