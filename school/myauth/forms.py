from django.contrib.auth.forms import *
from .models import *


class Regform(UserCreationForm):
    pass


class Logform(AuthenticationForm):
    pass


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']
