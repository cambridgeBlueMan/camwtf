from django.urls import path
from django.views.generic import TemplateView
from .import views

app_name='home'

urlpatterns = [
    path('', views.cambs, name = 'cambs_landing'),
    path('byTown/<int:theTown>/<int:lnRange>', views.byTown, name = 'by_town'),
    path('byDay/<int:theTown>/<int:lnRange>', views.byDay, name = 'by_day'),
]
