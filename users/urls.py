from django.urls import path, include
from users.views import LoginView, RegisterView, LoginAddView, profile
from django.contrib.auth.views import LogoutView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginAddView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
]
