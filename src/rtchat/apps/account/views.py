from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView

from rtchat.apps.account.forms import SignupForm


def logout(request: HttpRequest) -> HttpResponse:
    auth.logout(request)
    return redirect("account:login")


class LoginView(auth_views.LoginView):
    template_name = "account/login.html"


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "account/signup.html"

    def form_valid(self, form):
        """
        Override successful form submission to log the user in and redirect them.
        """
        self.object = form.save()
        auth.login(self.request, user=self.object)
        return redirect("chat:index")
