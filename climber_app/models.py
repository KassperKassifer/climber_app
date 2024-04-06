from django.db import models
from django.urls import reverse

# Create your models here.

class Gym(models.Model):
    #Fields
    ROUTE_TYPE_OPTIONS = (
    ('lead climbing', 'Lead climbing'),
    ('top rope', 'Top Rope'),
    ('bouldering', 'Bouldering'),
    ('crack climbing', 'Crack Climbing'),
    )
    name = models.CharField(max_length=200)
    email = models.CharField("Business Email", max_length=200)
    location = models.CharField("Location", max_length=200)
    route_types = models.CharField(
        max_length=100,
        choices=ROUTE_TYPE_OPTIONS,
        help_text='Select the route types offered by the gym',
    )    

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('gym-detail', args=[str(self.id)])


class Route(models.Model):
    #Fields
    level = models.CharField(max_length=20)
    route_setter = models.CharField(max_length=100)
    is_active = models.BooleanField(default = False)
    date_added = models.DateField()
    about = models.TextField(blank = True)
    wall_num = models.IntegerField(blank = True)
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, default=None, related_name='routes')

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.level + "-" + self.route_setter

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('route-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ["-date_added"]
