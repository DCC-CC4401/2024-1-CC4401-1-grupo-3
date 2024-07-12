
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Lugar, Reporte, Estudiante
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm, NuevoReporteForm
from django.core.paginator import Paginator
import json

def update_report(request):
    if request.method == "POST":
        if len(json.loads(request.body)) == 3:
            request_data = json.loads(request.body)
            reporte = Reporte.objects.get(pk=request_data['reporteId'])
            reporte_old_status = request_data['reporteOldStatus']
            reporte_new_status = request_data['reporteNewStatus']
            print(reporte_old_status, reporte_new_status, reporte)
            if reporte_old_status == reporte.estado and reporte_new_status != reporte.estado:
                reporte.estado = reporte_new_status
                reporte.save()
            return HttpResponseRedirect('/')

          
# Create your views here.   
def home(request):
    """
    ** Context **
    ``lugares``
        All the places in the database.
    ``reportes``
        All the reports in the database.

    ** Template **
    :template:`home.html`

    ** Description **
    If the request method is POST, the form is validated and the report is saved.
    If the request method is GET, the home page is rendered with the context to
    show all the places and the latest 5 reports. The template contains a form to create a new report.
    """
    if request.method == "POST":
        form_reporte = NuevoReporteForm(request.POST)
        if form_reporte.is_valid():
            cleaned_data = form_reporte.cleaned_data
            # Reporte.objects.create(**cleaned_data)
            rep = form_reporte.save(commit=False)
            estudiante = Estudiante.objects.get(id=request.user.id)
            rep.usuario = estudiante
            rep.save()
            rep = NuevoReporteForm()
        return HttpResponseRedirect('/')
    elif request.method == "GET":
        reportes = Reporte.objects.all()
        reportes = reportes.order_by('-hora')
        permisos = request.user.user_permissions.all()
        
        for permiso in permisos:
            print(f'{permiso.codename}')
        print(request.user.has_perm('can_change_status')) # La funcion has_perm() funciona mal!
        user_is_funcionario = request.user.has_module_perms('estadobuxef')  # Usuarios corrientes no tienes niun permiso
        if reportes.count() > 5:
            reportes = reportes[:5]
        context = {
            'lugares': Lugar.objects.all(), 
            'reportes': reportes,
            'user_is_funcionario': user_is_funcionario,
        }
        return render(request, "home.html", context)
    class Meta:
        app_label = 'estadobuxef'

def log_reg(request):
    """
    ** Context **
    ``login_form``
        The state of the login form.
    ``register_form``
        The state of the register form.

    ** Template **
    :template:`log-reg.html`

    ** Description **
    If the request method is POST and the login form is submitted, the form is validated
    and the user is authenticated. If the request method is POST and the register form is
    submitted, the form is validated and the user is created. If the request method is GET,
    the login and register forms are rendered. If no form is submitted, an error message is
    shown.
    """
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
                print(user)
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
                # UsuarioRegistrado.objects.create(usuario=user,)
                messages.success(request, 'You have signed up successfully.')
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid registration details')

    else:
        if request.GET.get('form') == 'signup':
            active_form = 0
                
    context = {
        'login_form': login_form,
        'register_form': register_form,
        'active_form': active_form,
    }
        
    return render(request,'log-reg.html', context=context)

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('log-reg')    

@login_required
def profile(request):
    user = request.user
    reportes = Reporte.objects.filter(usuario=user).order_by('-hora')
    return render(request, 'profile.html', {'user': user, 'reportes': reportes})    

def reports(request):
    """
    ** Context **
    ``data``
        All the reports in the database.

    ** Template **
    :template:`reports.html`

    ** Description **
    If the request method is GET, the reports page is rendered with the list
    of the reports in the database, the reports are going to be shown in sets of 
    5 with paginated lists.
    """
    if request.method == "GET":
        paginator = Paginator(Reporte.objects.all(), 5)
        page_number = request.GET.get('page')
        report_page = paginator.get_page(page_number)
        return render(request, "reports.html", {'data': report_page})

def lugar(request):
    nombre = request.GET.get('nombre')  
    lugar = get_object_or_404(Lugar, nombre=nombre)
    reportes = Reporte.objects.filter(lugar=lugar).all()
    return render(request, 'lugar.html', {'lugar': lugar, 'reportes': reportes})
