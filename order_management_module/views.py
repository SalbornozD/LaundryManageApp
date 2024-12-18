from django.shortcuts import render, redirect
from .models import Order, ItemOrder, ImageItemOrder
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404

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

def view_order(request, order_id):
    data = {}
    data['order'] = get_object_or_404(Order, id = order_id)
    items = ItemOrder.objects.filter(order = data['order'])
    data['items'] = {}

    for item in items:
        data['items'][item] = ImageItemOrder.objects.filter(item_order = item)

    return render(request, 'order_management_module/order.html', data)


def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order.client_name = request.POST.get('client_name')
        order.client_email = request.POST.get('client_email')
        order.save()

        existing_item_ids = []
        item_keys = [key for key in request.POST if key.startswith('description_')]
        for key in item_keys:
            unique_id = key.split('_')[1]
            description = request.POST.get(f'description_{unique_id}')
            detail = request.POST.get(f'detail_{unique_id}')

            item_order_id = request.POST.get(f'item_id_{unique_id}')
            if item_order_id:
                item_order = get_object_or_404(ItemOrder, id=item_order_id, order=order)
                item_order.description = description
                item_order.detail = detail
                item_order.save()
            else:
                item_order = ItemOrder.objects.create(
                    order=order,
                    description=description,
                    detail=detail
                )

            existing_item_ids.append(item_order.id)

            images = request.FILES.getlist(f'images_{unique_id}')
            for image in images:
                ImageItemOrder.objects.create(
                    item_order=item_order,
                    image=image
                )

        ItemOrder.objects.filter(order=order).exclude(id__in=existing_item_ids).delete()

        return redirect('home')

    items = ItemOrder.objects.filter(order=order).prefetch_related('imageitemorder_set')
    context = {
        'order': order,
        'items': items,
    }
    return render(request, 'order_management_module/order-form.html', context)

def delete_orders(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('home')