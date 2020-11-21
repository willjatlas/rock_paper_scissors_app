import unittest
from modules.game import Game 
from modules.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Matt Lucas", "paper")
        self.player_2 = Player("Bruce Lee", "scissors")
        self.player_3 = Player("Steve Buscemi", "paper")
        self.game = Game(self.player_1, self.player_2)
        self.game_2 = Game(self.player_1, self.player_3)

    def test_playing_rps(self):
        self.assertEqual("Bruce Lee wins by playing scissors", self.game.play_rps())

    def test_matching_choice_returns_none(self):
        self.assertIsNone(self.game_2.play_rps())