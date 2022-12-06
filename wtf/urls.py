from django.urls import path
from django.views.generic import TemplateView
from .import views
app_name='home'

urlpatterns = [
    # pre-defined class from Django
    #path('', TemplateView.as_view(template_name='home/main.html')),
    path('', views.main, name = 'main'),
    path('intergroup/<int:ig>', views.intergroup, name = 'intergroup'),
    path('town/<int:town>', views.town, name = 'town_id'),
    path('town/<str:town>', views.town, name = 'town'),
]
