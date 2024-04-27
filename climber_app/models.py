from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    email = models.EmailField("Business Email", max_length=200, blank=True)
    location = models.CharField("Location", max_length=200)
    about = models.TextField(blank=True)
    top_rope_climbing = models.BooleanField(default=False)
    lead_climbing = models.BooleanField(default=False)
    bouldering = models.BooleanField(default=False)
    crack_climbing = models.BooleanField(default=False)
    membership_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    daily_price = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    gym_image = models.ImageField(null=True, blank=True, upload_to="images/")

    #Connect to permission group
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

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
    wall_num = models.IntegerField(blank = True, default=None, null=True)
    route_type = models.CharField(max_length=20, default="Bouldering")
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, default=None, related_name='routes')

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.level + "-" + self.route_setter

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('view-route', args=[str(self.gym.id), str(self.id)])
    
    class Meta:
        ordering = ["-date_added"]
