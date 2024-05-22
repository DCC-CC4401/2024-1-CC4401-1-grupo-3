from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NuevoReporteForm, Lugar, Reporte
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm


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
    show all the places and reports. The template contains a form to create a new report.
    """
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

    if request.method == 'POST' and 'login-form' not in request.POST and 'signup-form' not in request.POST:
        messages.error(request, f'Invalid username or password')
        return render(request, 'log-reg.html', {'login_form': login_form, 'register_form': register_form})

    if request.method == 'POST' and 'login-form' in request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return HttpResponseRedirect('/')

        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'log-reg.html', {'login_form': login_form, 'register_form': register_form})

    if request.method == 'POST' and 'signup-form' in request.POST:
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
        return render(request, 'log-reg.html', {'login_form': login_form, 'register_form': register_form})


def reports(request):
    """
    ** Context **
    ``data``
        All the reports in the database.

    ** Template **
    :template:`reports.html`

    ** Description **
    If the request method is GET, the reports page is rendered with the list
    of all the reports in the database.
    """
    if request.method == "GET":
        return render(request, "reports.html", {'data': Reporte.objects.all()})
