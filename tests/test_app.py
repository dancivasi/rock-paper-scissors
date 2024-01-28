from app import Player, CHOICES, Game
import pytest


@pytest.fixture()
def game():
    player1 = Player("Simon", "Vasile")
    player2 = Player("Adrian", "Moloce")
    player1.draw()
    player2.draw()
    game = Game()
    return game.decide_winner(player1, player2)

def test_check_if_playerone_draws_something():
    assert Player("Simon", "Vasile").draw() in CHOICES

def test_if_playertwo_draws_something():
    assert Player("Moloce", "Adrian").draw() in CHOICES

def test_if_game_can_tie_or_win(game):
    assert game == "Tie" or game == "Simon Vasile Wins" or game == "Adrian Moloce Wins"