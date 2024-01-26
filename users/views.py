from django.contrib.auth.views import LoginView as BaseLoginView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import CreateView

from config import settings
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

    def form_valid(self, form):
        new_pass = form.password1
        new_user = form.save()
        send_mail(
            subject='Привет чушпан',
            message=f'Твой пароль: {new_pass}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def generate_password(request):
    new_pass = User.objects.make_random_password()

    return new_pass


class LoginAddView(LoginView):
    template_name = 'users/signin_add.html'
