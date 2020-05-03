from django.test import TestCase, SimpleTestCase
import unittest
from unittest.mock import MagicMock
from django.shortcuts import reverse, resolve
from .models import Game
from .models import Recommendation
from blog.views import Po

#
# class HomePageTests(SimpleTestCase):
#     def test_home_status_code(self):
#         response = self.client.get('/')
#         self.assertEquals(response.status_code, 200)
    
#     def test_home_url_name(self):
#         response = self.client.get(reverse('home'))
#         self.assertEquals(response.status_code, 200)

#     def test_correct_template(self):
#         response = self.client.get(reverse('home'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'home.html')

    

# class BasicTest(TestCase):
#     def test_fields(self):
#         game = Game()
#         Game.title = "TechMan"
#         Game.information = "BlockOfText"
#         game.save()

#         record = Game.objects.get(pk=1)
#         self.assertQuerysetEqual(record,game)


#class TestUrls(SimpleTestCase):

  