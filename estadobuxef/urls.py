from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("log-reg", views.log_reg, name="log-reg"),
    path("reports", views.reports, name="reports"),
    path("logout", views.sign_out, name="logout"),
    path('profile', views.profile, name='user-profile')
]
