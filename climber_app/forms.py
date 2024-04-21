from django.forms import ModelForm
from django import forms
from .models import Gym, Route
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class GymForm(ModelForm):
    class Meta:
        model = Gym
        fields = ('__all__')
        exclude = ['user']

class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = ('level', 'route_setter', 'is_active', 'date_added', 'about', 'wall_num', 'route_type')
        widgets = {
            'date_added': forms.DateInput(attrs={'type': 'date'})
        }

#Registration page
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

