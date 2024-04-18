from django.forms import ModelForm
from .models import Gym, Route
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class GymForm(ModelForm):
    class Meta:
        model = Gym
        fields = ('name', 'email', 'location', 'about', 'top_rope_climbing', 'lead_climbing', 'bouldering', 'crack_climbing', 'membership_price', 'daily_price')

class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = ('level', 'route_setter', 'is_active', 'date_added', 'about', 'wall_num', 'route_type')

#Registration page
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']