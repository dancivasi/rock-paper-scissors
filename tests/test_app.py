from app import RockPaperScissors, Player
import pytest

@pytest.fixture()
def game():
    game = RockPaperScissors()
    game.player1 = Player("Vasi")
    game.player2 = Player("Adrian")
    return game

@pytest.mark.parametrize(
    "draw1, draw2, expected",
    [
        ("ROCK", "SCISSORS", "Vasi wins with ROCK"),
        ("PAPER", "ROCK", "Vasi wins with PAPER"),
        ("SCISSORS", "PAPER", "Vasi wins with SCISSORS"),
        ("ROCK", "ROCK", "Tie"),
        ("ROCK", "paper", "Adrian wins with PAPER"),
        ("asdasidjasiodajsd", "aksjdhaiksdhiasd", "invalid options")
    ]
)
def test_rock_beat_scissors(game, draw1, draw2, expected):
    assert game.play(draw1, draw2) == expected