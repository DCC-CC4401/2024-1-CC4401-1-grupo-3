from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import NuevoReporteForm, Lugar, Reporte


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
    return render(request, "log-reg.html")

def reports(request):
    if request.method == "GET":
        return render(request, "reports.html", {'data': Reporte.objects.all()})

