from django.urls import path
from . import views
from django.views.generic import TemplateView
"""
The most direct way to use generic views is to create them directly in your URLconf. 
If you’re only changing a few attributes on a class-based view, you can pass them into 
the as_view() static class method call itself:

Then we need to add this new view into our URLconf. TemplateView is a class, not a f
unction, so we point the URL to the as_view() class method instead, which provides a 
function-like entry to class-based views:


"""
app_name='authz'
urlpatterns = [
    path('', TemplateView.as_view(template_name='authz/main.html')),
    path('open', views.OpenView.as_view(), name='open'),
    path('apereo', views.ApereoView.as_view(), name='apereo'),
    path('manual', views.ManualProtect.as_view(), name='manual'),
    path('protect', views.ProtectView.as_view(), name='protect'),
    path('python', views.DumpPython.as_view(), name='python'),
]
