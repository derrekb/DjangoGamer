from django.test import TestCase
import unittest
from unittest.mock import MagicMock
from .models import Game
from .models import Recommendation

# Create your tests here.
class GameTestCases(TestCase):
    def setUp(self):
        Game.object.create(title = "Call of Juarez" ,information = 'pistola pistola disparar disparar')
        Game.object.create(title = "Call of Duty" ,information = 'gun gun shoot shoot' )


    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        COJ = Game.objects.get(name="Call of Juarez")
        COD = Game.objects.get(name="Call of Duty")
        self.assertEqual(COJ.information(), 'pistola pistola disparar disparar')
        self.assertEqual(COD.information(), 'gun gun shoot shoot')