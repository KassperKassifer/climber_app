from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, Group
from climber_app.models import Gym, Route
import json
from django.urls.exceptions import NoReverseMatch

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.gym = Gym.objects.create(name = 'Gym1', location = 'location', user = self.user)
        self.route = Route.objects.create(level='V1',  route_setter='guy', date_added='2024-01-01', route_type='type', gym=self.gym)
        self.factory = RequestFactory()
        self.group = Group.objects.filter(name='gym_role').first()


        self.index_url = reverse('index')
        self.gyms_url = reverse('gyms')
        self.route_detail_url = reverse('view-route', kwargs={'gym_id': self.gym.id, 'pk': self.route.id})
        self.route_update_url = reverse('update-route', kwargs={'gym_id': self.route.gym.id, 'pk': self.route.id})
        

    # Test index view
    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'climber_app/index.html')

    # Test GymViewList view
    def test_gym_list_GET(self):
        response = self.client.get(self.gyms_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'climber_app/gym_list.html')

    # Test RouteUpdateView to ensure that an authenticated user is redirected to the route_form
    def test_route_update_GET(self):
        user = self.user
        user.groups.add(self.group)

        self.client.force_login(user)  # Log in the user
        response = self.client.get(self.route_update_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'climber_app/route_form.html')
