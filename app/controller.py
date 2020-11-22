from app import app 
from flask import render_template, request, redirect
from app.modules.game import Game
from app.modules.player import Player

@app.route('/')
def home():
    return render_template("home.html", title="Home: ")

@app.route('/<choice_1>/<choice_2>')
def play_rps(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    game = Game(player_1, player_2)
    winner = game.play_rps()
    return f'{winner}'

@app.route('/singleplay')
def single_player():
    return render_template("singleplay.html", title="Single Player: ")

@app.route('/multiplay')
def multiplayer():
    return render_template("multiplay.html", title="Multiplayer: ")

@app.route('/play', methods=["POST"])
def single_play():
    player_1 = Player(request.form["player_1_name"], request.form["player_1_choice"])
    player_2 = Player(None, None)
    game = Game(player_1, player_2)
    final_winner = game.play_rps()
    return redirect (f'/winner/{final_winner}')

# Could use sessions with a key, or make a database, but ¯\_(ツ)_/¯, it works.
@app.route('/winner/<final_winner>')
def winner(final_winner):
    return render_template("winner.html", winner=final_winner, title="WINNER: ")

