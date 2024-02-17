from django.contrib.auth.views import LoginView as BaseLoginView
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, View
from config import settings
from users.forms import UserForm, LoginForm, ProfileUpdateForm
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


class ProfileView(View):
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        user_news = News.objects.filter(author=user)
        user_realty = Realty.objects.filter(owner=user)
        user_realty = user_realty.prefetch_related('photo')
        context = {
            'user': user,
            'user_news': user_news,
            'user_realty': user_realty
        }
        return render(request, self.template_name, {'object_list': context})


class ProfileUpdateView(UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'users/update_profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
