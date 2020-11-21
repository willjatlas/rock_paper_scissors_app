class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


    def player_wins(self, player):
        return f'{player.name} wins by playing {player.choice}'
        

    def play_rps(self):
        if self.player_1.choice == self.player_2.choice:
            return None
        elif self.player_1.choice == "rock":
            if self.player_2.choice == "scissors":
                return self.player_wins(self.player_1)
            elif self.player_2.choice == "paper":
                return self.player_wins(self.player_2)
        elif self.player_1.choice == "paper":
            if self.player_2.choice == "rock":
                return self.player_wins(self.player_1)
            elif self.player_2.choice == "scissors":
                return self.player_wins(self.player_2)
        elif self.player_1.choice == "scissors":
            if self.player_2.choice == "paper":
                return self.player_wins(self.player_1)
            elif self.player_2.choice == "rock":
                return self.player_wins(self.player_2)
        
         

