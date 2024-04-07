from django.urls import path, include
from . import views


urlpatterns = [
    #path function defines a url pattern
    #'' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>.
    #connect path to portfolio_app urls
    path('', views.index, name="index"),
    path('gyms/', views.GymViewList.as_view(), name="gyms"),
    path('gym-detail/<int:pk>', views.GymDetailView.as_view(), name="gym-detail"),
    path('gym/<int:gym_id>/create-route/', views.createRoute, name="create-route"),
    path('gym/<int:gym_id>/update-route/<int:pk>', views.RouteUpdateView.as_view(), name="update-route"),
    path('gym/<int:gym_id>/route/<int:pk>/', views.RouteDetailView.as_view(), name="view-route"),
    path('gym/<int:gym_id>/route/<int:pk>/delete/', views.RouteDeleteView.as_view(), name="delete-route"),
    


    #Stub page for login and logout views
	path('login/', views.stub, name="login"),
    path('logout/', views.stub, name="logout"),
]
