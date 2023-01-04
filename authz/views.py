from django.shortcuts import render, redirect
from django.views import View
"""
A view is a callable which takes a request and returns a response. This can be more than just a 
function.

All views inherit from the View class, which handles linking the view into the URLs, HTTP method 
dispatching and other common features.

 RedirectView provides a HTTP redirect, and TemplateView extends the base class to make it 
 also render a template.

"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.http import urlencode

"""
The second, more powerful way to use generic views is to inherit from an existing 
view and override attributes (such as the template_name) or methods (such as 
get_context_data) in your subclass to provide new values or methods.

"""
class OpenView(View) :
    def get(self, request):
        return render(request, 'authz/main.html')

class ApereoView(View) :
    def get(self, request):
        return render(request, 'authz/main.html')

class ManualProtect(View) :
    """
    User objects are the core of the authentication system. They typically 
    represent the people interacting with your site and are used to enable things 
    like restricting access, registering user profiles, associating content with 
    creators etc. Only one class of user exists in Django’s authentication framework, 
    i.e., 'superusers' or admin 'staff' users are just user objects with special 
    attributes set, not different classes of user objects.

    """
    def get(self, request):
        """
        We want to transfer the user to a login page from many pages in our application 
        and when they successfully log in, we want to bring them back to our page or some 
        other page.

        The "next=" parameter tells login or logout  where to redirect the user after login
        
        To allow us to control the look and feel of the login page we must provide a template 
        called "registration/login.html"
        Django describes what needs to be in this template
        We can put this in any of our application templates folders
        
        """
        if not request.user.is_authenticated :
            loginurl = reverse('login')+'?'+urlencode({'next': request.path})
            return redirect(loginurl)
        return render(request, 'authz/main.html')

class ProtectView(LoginRequiredMixin, View) :
    """
    When using class-based views, you can achieve the same behavior as with login_required 
    by using the LoginRequiredMixin. This mixin should be at the leftmost position in the 
    inheritance list.

    """
    def get(self, request):
        return render(request, 'authz/main.html')

from django.http import HttpResponse

class DumpPython(View) :
    def get(self, req):
        resp = "<pre>\nUser Data in Python:\n\n"
        resp += "Login url: " + reverse('login') + "\n"
        resp += "Logout url: " + reverse('logout') + "\n\n"
        if req.user.is_authenticated:
            resp += "User: " + req.user.username + "\n"
            resp += "Email: " + req.user.email + "\n"
        else:
            resp += "User is not logged in\n"

        resp += "\n"
        resp += "</pre>\n"
        resp += """<a href="/authz">Go back</a>"""
        return HttpResponse(resp)


# https://docs.djangoproject.com/en/3.0/topics/auth/default/#authentication-in-web-requests

