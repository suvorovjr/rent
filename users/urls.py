from django.urls import path
from users.views import LoginView, RegisterView
from django.contrib.auth.views import LogoutView
from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(), name='auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', RegisterView.as_view(), name='signup'),
]
