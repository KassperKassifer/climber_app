from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.urls import reverse_lazy

#Catch all for pages not yet done
def stub(request):
    #Render the stub.html page
    return render(request, 'climber_app/stub.html')


# Create your views here.
def index(request):
    # Render the HTML template index.html with the data in the context variable.
    
    # Retrieve all Gym objects
    gyms = Gym.objects.all()
    
    # Filter active routes for each gym
    gym_active_routes = []
    for gym in gyms:
        active_routes = gym.routes.filter(is_active=True)
        gym_active_routes.append((gym, active_routes))
    
    print("active route query set", gym_active_routes)
    return render( request, 'climber_app/index.html', {'gym_active_routes':gym_active_routes})


# Implement classes that inherit from a generic view
# this will query the database to get all records
class GymViewList(generic.ListView):
    model = Gym

class GymDetailView(generic.DetailView):
    model = Gym

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gym = self.get_object()
        true_fields = [field.verbose_name for field in Gym._meta.fields if isinstance(field, models.BooleanField) and getattr(gym, field.name)]        
        context['true_fields'] = true_fields
        return context