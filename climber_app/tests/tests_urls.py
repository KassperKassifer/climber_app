from django.test import SimpleTestCase
from django.urls import reverse, resolve
from climber_app.views import GymUpdateView, GymCreateView, RouteDeleteView, RouteUpdateView, RouteDetailView,  GymDetailView, GymViewList, createRoute, index

class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)
    
    def test_gyms_url_resolves(self):
        url = reverse('gyms')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, GymViewList)

    def test_gym_detail_url_resolves(self):
        url = reverse('gym-detail', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, GymDetailView)

    def test_create_gym_url_resolves(self):
        url = reverse('create-gym')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, GymCreateView)

    def test_create_route_url_resolves(self):
        url = reverse('create-route', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, createRoute)

    def test_update_route_url_resolves(self):
        url = reverse('update-route', kwargs={'gym_id':'1', 'pk': '1'})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, RouteUpdateView)

    