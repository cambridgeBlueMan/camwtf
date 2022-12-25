from django.urls import path
from django.views.generic import TemplateView
from .import views

app_name='home'

urlpatterns = [
    # pre-defined class from Django
    #path('', TemplateView.as_view(template_name='home/main.html')),
    #path('', views.main, name = 'main'),
    #path('main', views.main, name = 'main'),
    # path('intergroup/<int:ig>', views.intergroup, name = 'intergroup'),
    path('', views.cambs, name = 'cambs_landing'),
    path('ajax/<int:theTown>', views.ajax, name = 'ajax'),
    path('ajaxByDay/<int:theTown>', views.ajaxByDay, name = 'ajax_by_day'),
    #path('town/<int:town>', views.town, name = 'by_town_id'),
    #path('town/<str:town>', views.town, name = 'by_town'),
    #path('day/<int:ig>', views.byDay, name = 'by_day'),
    #path('bs4', views.bs4, name = 'bs4'),

]
