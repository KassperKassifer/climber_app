from django.urls import path
from . import views


urlpatterns = [
    path('login_user/', views.login_user, name='custom-login'),
    path('logout_user/', views.customLogout, name='custom-logout'),
]