class Game:

    def __init__(self):
        pass


    def player_wins(self, player):
        return f'{player.name} wins by playing {player.choice}'
        

    def play_rps(self, player_1, player_2):
        if player_1.choice == player_2.choice:
           return None
        elif player_1.choice == "rock":
            if player_2.choice == "scissors":
                self.player_wins(player_1)
            elif player_2.choice == "paper":
                self.player_wins(player_2)
        elif player_1.choice == "paper":
            if player_2.choice == "rock":
                self.player_wins(player_1)
            elif player_2.choice == "scissors":
                self.player_wins(player_2)
        elif player_1.choice == "scissors":
            if player_2.choice == "paper":
                self.player_wins(player_1)
            elif player_2.choice == "rock":
                self.player_wins(player_2)
        
         

