from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import RegisterForm


# Реєстрація
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = "/accounts/login"
    http_method_names = ["get", "post"]


# Логін
class CustomLoginView(LoginView):
    template_name = "login.html"


# Логаут
class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/table-booking/home/")  # обов'язково абсолютний шлях

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("/table-booking/home/")