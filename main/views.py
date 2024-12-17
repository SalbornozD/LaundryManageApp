from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from order_management_module.models import Order, ItemOrder, ImageItemOrder

def index(request):
    data = {}

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            
            try:
                user = User.objects.get(username=username)
                
                if not user.is_active:
                    data['error_message'] = "Tu cuenta está inactiva. Por favor, verifica tu correo para activarla."
                
                else:
                    user = authenticate(request, username=username, password=password)
                    if user is None: data["error_message"] = "El nombre de usuario o la contraseña no son correctos."
            
                    else:
                        return redirect('home')
                        
            except User.DoesNotExist:
                data["error_message"] = "El nombre de usuario o la contraseña no son correctos."
    
    else:
        login_form = LoginForm()
    
    data["form"] = login_form
    return render(request, 'main/index.html', data)

@login_required
def home(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    date_filter = request.GET.get('date', '')

    orders = Order.objects.filter(status__in=['3', '4'])

    if search_query: #Filtro por nombre de cliente
        orders = orders.filter(client_name__icontains=search_query)

    if status_filter: # Filtro por estado
        orders = orders.filter(status=status_filter)

    if date_filter: # Filtro por fecha de recepción
        orders = orders.filter(receipt_date_time__date=date_filter)

    data = {
        'user': request.user,
        'orders': orders,
    }

    return render(request, 'main/home.html', data)