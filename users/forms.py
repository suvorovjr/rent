from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from users.models import User
from django import forms


class StylesMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input'


class LoginForm(StylesMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserForm(StylesMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class ProfileUpdateForm(StylesMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'telegram', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
