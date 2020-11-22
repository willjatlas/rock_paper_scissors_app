import random

class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.choice_list = ["rock", "paper", "scissors"]


    def player_wins(self, player):
        """ Helper method to return the winner string """
        return f'{player.name} wins by playing {player.choice}'
    
    def check_for_cpu_player(self):
        """ Check to see if this is a single player game """ 
        if self.player_2.choice == None:
            self.generate_cpu_player(self.player_2)

    def generate_cpu_player(self, cpu):
        """ Make the choice for the computer player """ 
        cpu.choice = random.choice(self.choice_list)
        cpu.name = "A (°_o) Definitely Human (°_o) I"

    def play_rps(self):
        self.check_for_cpu_player()
        """ Method of logic for rps game"""
        if self.player_1.choice == self.player_2.choice:
            return "It's a draw!!!"
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
        
         

