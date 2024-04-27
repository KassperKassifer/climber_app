from selenium import webdriver
from django.test import LiveServerTestCase
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.urls import reverse


class Hosttest(LiveServerTestCase):
    # A simple test to ensure that the home page is the index page. Mostly for practice with selenium
    def testHomePage(self):
        driver = webdriver.Chrome()

        driver.get('http://localhost:8000/')

        time.sleep(3)

        assert "Climb Companion" in driver.title

class LoginFormTest(LiveServerTestCase):
    # tests that if valid credentials are used to login from the nav bar, they will be redirected to the home page
    # that will now show their username on the page
    def testForm(self):
        driver = webdriver.Chrome()

        driver.get('http://localhost:8000/members/login_user/?next=/')
        time.sleep(3)

        user_name = driver.find_element(By.NAME, 'username')
        user_password = driver.find_element(By.NAME, 'password')
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="login"]')

        user_name.send_keys('Newbie')
        user_password.send_keys('nebiscuitsbro//52*ie')
        submit.send_keys(Keys.RETURN)
        time.sleep(3)

        assert 'Newbie' in driver.page_source

class RouteFormTest(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    # tests that if an unauthorized user tries to update a route, they will be redirected to a login page
    def test_route_update_unauthorized_redirect(self):
        self.driver.get('http://localhost:8000/gym/9/update-route/10')      
        time.sleep(3)

        # Verify that the user is redirected to the login page
        self.assertIn('login', self.driver.current_url)

    # tests that if an authorized user tries to update a route, they will be able to
    def test_route_update_authorized(self):
        self.driver.get('http://localhost:8000/gym/9/update-route/10')
        
        user_name = self.driver.find_element(By.NAME, 'username')
        user_password = self.driver.find_element(By.NAME, 'password')
        submit = self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="login"]')

        user_name.send_keys('Newbie')
        user_password.send_keys('nebiscuitsbro//52*ie')
        submit.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # Attempt to access the route update page
        self.driver.get('http://localhost:8000/gym/9/update-route/10')
        time.sleep(3)

        # Verify that the user is on update route form
        self.assertIn('update-route', self.driver.current_url)
