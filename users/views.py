from django.contrib.auth.views import LoginView as BaseLoginView
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from config import settings
from users.forms import UserForm, LoginForm
from django.urls import reverse_lazy
from users.models import User
from news.models import News
from realty.models import Realty


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
        new_user = form.save()
        send_mail(
            subject='Привет',
            message='Приветствую на площадке}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class LoginAddView(LoginView):
    template_name = 'users/signin_add.html'


class ProfileListView(ListView):
    model = Realty
    template_name = 'realty/profile.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(owner=user)
        return queryset
