from django.http import HttpResponse
from django.shortcuts import render
from .models import NuevoReporteForm


# Create your views here.
def home(request):
    if request.method == "POST":
        form_reporte = NuevoReporteForm(request.POST)
        if form_reporte.is_valid():
            reporte = form_reporte.cleaned_data
            reporte.save()
    elif request.method == "GET":
        return render(request, "home.html", {'lugares': [["F10", "0"]]})


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")
