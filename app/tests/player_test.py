import unittest
from app.modules.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Chris Pratt", "rock")

    def test_player_has_name(self):
        self.assertEqual("Chris Pratt", self.player.name)