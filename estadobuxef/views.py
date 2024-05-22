from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NuevoReporteForm, Lugar, Reporte
from .forms import LoginForm, RegisterForm



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
    if request.method == 'POST' and 'login-form' in request.POST:
        form = LoginForm(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return HttpResponseRedirect('/')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'log-reg.html',{'login_form': login_form, 'register_form': register_form})
        
    if request.method=='POST' and 'signup-form' in request.POST:
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'log-reg.html', {'login_form': login_form, 'register_form': register_form})
            
    elif request.method == "GET":
        login_form = LoginForm()
        register_form = RegisterForm()
        return render(request,'log-reg.html', {'login_form': login_form, 'register_form': register_form})

def reports(request):
    if request.method == "GET":
        return render(request, "reports.html", {'data': Reporte.objects.all()})

