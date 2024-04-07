from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import RouteForm
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


# Create Route form view
def createRoute(request, gym_id):
    form = RouteForm()
    gym = Gym.objects.get(pk=gym_id)

    if request.method == "POST":
        # Create new dictionary with form data and gym_id
        route_data = request.POST.copy()
        route_data['gym_id'] = gym_id
        form = RouteForm(route_data)
        if form.is_valid():
            # Save the form without comitting to database
            route = form.save(commit=False)
            # Set the gym relationship
            route.gym = gym
            route.save()

            # Redirect back to the portfolio detail page
            return redirect('gym-detail', gym_id)
    context = {'form': form}
    return render(request, 'climber_app/route_form.html', context)


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
    
class RouteDetailView(generic.DetailView):
    model = Route
    template_name = 'climber_app/route_detail.html'
    context_object_name = 'route'

    def get_queryset(self):
        queryset = super().get_queryset()
        gym_id = self.kwargs['gym_id']
        pk = self.kwargs['pk']
        return queryset.filter(gym_id=gym_id, pk=pk)
    
class RouteUpdateView(generic.edit.UpdateView):
    model = Route
    fields = ['level', 'is_active', 'about']
    template = 'climber_app/route_form.html'

    def get_queryset(self):
        # Filter the queryset based on the URL parameters
        queryset = super().get_queryset()
        gym_id = self.kwargs['gym_id']
        pk = self.kwargs['pk']
        return queryset.filter(gym_id=gym_id, pk=pk)
    
    def get_success_url(self):
        gym_id = self.kwargs['gym_id']
        return reverse('gym-detail', kwargs={'pk': gym_id})

class RouteDeleteView(generic.edit.DeleteView):
    model = Route
    template_name = 'climber_app/route_delete.html'
    context_object_name = 'route' #'route' will refer to the route object in route_delete.html

    def get_success_url(self):
        gym_id = self.kwargs['gym_id']
        return reverse('gym-detail', kwargs={'pk': gym_id})
    
