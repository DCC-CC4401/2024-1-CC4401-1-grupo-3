from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lugar, Reporte
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, NuevoReporteForm

# Create your views here.
def home(request):
    if request.method == "POST":
        form_reporte = NuevoReporteForm(request.POST)
        if form_reporte.is_valid():
            cleaned_data = form_reporte.cleaned_data
            # Reporte.objects.create(**cleaned_data)
            form_reporte.save()
            form_reporte = NuevoReporteForm()
        return HttpResponseRedirect('/')
    elif request.method == "GET":
        return render(request, "home.html", {'lugares': Lugar.objects.all(), 'reportes': Reporte.objects.all()})

def log_reg(request):
    login_form = LoginForm()
    register_form = RegisterForm()
    active_form = 1 #default 1 for login

    if request.method == 'POST':
        if 'login_form' in request.POST:
            login_form = LoginForm(request.POST)
            active_form = 1
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                if user:
                    login(request, user)
                    messages.success(request,f'Hi {username.title()}, welcome back!')
                    return redirect('home')
            
            messages.error(request,f'Invalid username or password')
        
        else:
            register_form = RegisterForm(request.POST) 
            active_form = 0
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                messages.success(request, 'You have signed up successfully.')
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid registration details')
                
    context = {
        'login_form': login_form,
        'register_form': register_form,
        'active_form': active_form,
    }
        
    return render(request,'log-reg.html', context=context)

def reports(request):
    if request.method == "GET":
        return render(request, "reports.html", {'data': Reporte.objects.all()})

