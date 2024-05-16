from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def log_reg(request):
    return render(request, "log-reg.html")

def report(request):
    return render(request, "reports.html")
