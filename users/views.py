from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, View
from users.services import send_verification_password
from users.forms import UserForm, LoginForm, ProfileUpdateForm
from django.urls import reverse_lazy, reverse
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
        self.object = form.save()
        self.object.verification_token = get_random_string(30)
        verification_link = f'http://{get_current_site(self.request)}/users/confirm/{self.object.verification_token}'
        send_verification_password(self.object.email, verification_link)
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


def activate_user(request, token):
    user = User.objects.get(verification_token=token)
    user.verification_token = ''
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))
