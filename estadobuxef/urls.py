from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("log-reg", views.log_reg, name="log-reg"),
    path("reports", views.reports, name="reports"),
    path("logout", views.sign_out, name="logout"),
    path('profile', views.profile, name='user-profile'),
    path("update-report", views.update_report, name="update-report"),
    path("like-place", views.like_place, name="like-place"),
    path("lugar/", views.lugar, name="lugar"),
]
