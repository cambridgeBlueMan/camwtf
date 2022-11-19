from django.urls import path
from wtf import views

urlpatterns = [
    path("", views.home, name="home"),
]