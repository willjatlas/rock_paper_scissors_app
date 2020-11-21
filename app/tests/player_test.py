import unittest
from modules.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Chris Pratt", "rock")

    def test_player_has_name(self):
        self.assertEqual("Chris Pratt", self.player.name)

    def test_player_has_choice(self):
        self.assertEqual("rock", self.player.choice)