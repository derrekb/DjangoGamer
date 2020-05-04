from django.test import TestCase, SimpleTestCase
import unittest
from unittest.mock import MagicMock
from django.shortcuts import reverse
from .models import Game
#from blog.models import title, description, genres ,tags ,developers, publishers ,platforms, places_to_purchase




class GameTest(TestCase):
    def create_game(self, title = "Zoldo", description = "Zoldo must save Lonk. Save him"):
        return Game.objects.create(title = title,
        description =  description
        )

        def test_game_creation(self):
            a = self.create.game()
            self.assertTrue(isinstance(a, Game))
            self.assertEqual(a. __str__(), a.title)



# class GameTestCase(TestCase):
#     def setUp(self):
#       Game.objects.create(name="laststory", description="sword")
#       Game.objects.create(name="finalfantasy", description="katana")

#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         laststory = Game.objects.get(name="laststory")
#         finalfantasy = Game.objects.get(name="finalfantasy")
#         self.assertEqual(laststory.description(), "sword")
#         self.assertEqual(finalfantasy.description(), "katana")





 



















































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

  