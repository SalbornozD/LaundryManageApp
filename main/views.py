from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

def index(request):
    data = {}

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print("Exito") #Redireccionar a Home.
            else:
                print("Usuario o contraseña incorrectos.") # Mensaje de error.
    
    else:
        login_form = LoginForm()
    
    data["form"] = login_form
    return render(request, 'main/index.html', data)