from django.urls import path
from django.views.generic import TemplateView
from .import views
app_name='home'

urlpatterns = [
    # pre-defined class from Django
    #path('', TemplateView.as_view(template_name='home/main.html')),
    path('', views.tags, name = 'tags'),
    path('tags/<int:tagNum>', views.tags, name = 'tags'),

]
