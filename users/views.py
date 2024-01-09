from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView
from users.forms import UserForm, LoginForm
from django.urls import reverse_lazy
from users.models import User


class LoginView(BaseLoginView):
    model = User
    form_class = LoginForm
    template_name = 'users/signin.html'


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:auth')
    template_name = 'users/signup.html'
