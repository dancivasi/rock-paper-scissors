from app import Player, choices
import pytest



def test_check_if_playerone_draws_something():
    player1 = Player("Simon", "Vasile")
    draw = player1.draw()
    assert draw in choices

def test_if_playertwo_draws_something():
    player2 = Player("Moloce", "Adrian")
    draw = player2.draw()
    assert draw in choices

