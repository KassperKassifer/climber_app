from django.test import TestCase
from climber_app.models import Gym, Route
from django.contrib.auth.models import User


class TestModels(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.gym = Gym.objects.create(
            name='Test Gym',
            email='test@example.com',
            location='Test Location',
            about='Test About',
            top_rope_climbing=True,
            lead_climbing=False,
            bouldering=True,
            crack_climbing=False,
            membership_price=50.00,
            daily_price=10.00,
            user=self.user
        )
        self.route = Route.objects.create(
            level='Test Level',
            route_setter='Test Setter',
            is_active=True,
            date_added='2022-01-01',
            about='Test About',
            wall_num=1,
            route_type='Bouldering',
            gym=self.gym
        )

    # Gym Model Tests
    def test_gym_string_representation(self):
        self.assertEqual(str(self.gym), 'Test Gym')

    def test_gym_get_absolute_url(self):
        self.assertEqual(self.gym.get_absolute_url(), '/gym-detail/{}'.format(self.gym.id))

    def test_membership_price_default(self):
        self.assertEqual(self.gym.membership_price, 50.00)

    def test_user_association(self):
        self.assertEqual(self.gym.user, self.user)

    # Route Model Tests
    def test_route_string_representation(self):
        self.assertEqual(str(self.route), 'Test Level-Test Setter')

    def test_route_get_absolute_url(self):
        self.assertEqual(self.route.get_absolute_url(), '/gym/{}/route/{}/'.format(self.gym.id, self.route.id))