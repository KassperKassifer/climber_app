from django.test import TestCase
from climber_app.forms import GymForm
from django.contrib.auth.models import User

class TestForms(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')


    def test_gym_form_valid_data(self):
        form = GymForm(data ={
            'name': 'gym1',
            'email': 'example@test.com',
            'location': 'test location',
            'top_rope_climbing': 'True',
            'membership_price': 50.00,
            'daily_price': 18.00,
            'user': self.user
        })

        self.assertTrue(form.is_valid())

    def test_gym_form_no_data(self):
        form = GymForm(data={})

        self.assertFalse(form.is_valid())
        print(form.errors)
        self.assertEquals(len(form.errors), 4)