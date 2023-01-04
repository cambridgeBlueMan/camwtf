"""camwtf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("wtf.urls")),
    path("authz", include("authz.urls")),

    path('admin/', admin.site.urls),
    """We need to add a path to the code that gives us login and logout urls
    We can reverse lookup these urls using the 'login' and 'logout' view names
    """
    path('accounts/', include('django.contrib.auth.urls')),

]
