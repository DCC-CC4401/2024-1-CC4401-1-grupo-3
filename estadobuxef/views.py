from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import NuevoReporteForm, Lugar, Reporte


# Create your views here.
def home(request):
    if request.method == "POST":
        form_reporte = NuevoReporteForm(request.POST)
        print(form_reporte.is_valid())
        if form_reporte.is_valid():
            cleaned_data = form_reporte.cleaned_data
            # Reporte.objects.create(**cleaned_data)
            form_reporte.save()
        return HttpResponseRedirect('')
    elif request.method == "GET":
        return render(request, "home.html", {'lugares': Lugar.objects.all(), 'reportes': Reporte.objects.all()})


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")
