from django.urls import path
from users.views import LoginView, RegisterView, LoginAddView, ProfileView, ProfileUpdateView, activate_user
from django.contrib.auth.views import LogoutView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginAddView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update', ProfileUpdateView.as_view(), name='profile_update'),
    path('confirm/<str:token>', activate_user, name='confirm')
]
