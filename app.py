RPS_WINNERS = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}


class Player:
    def __init__(self, name):
        self.name = name


class RockPaperScissors:
    player1: Player
    player2: Player

    def play(self, draw1: str, draw2: str) -> str:
        draw1 = draw1.upper()
        draw2 = draw2.upper()
        if draw1 not in RPS_WINNERS or draw2 not in RPS_WINNERS:
            return "invalid options"
        if draw1 == draw2:
            return "Tie"
        elif draw2 == RPS_WINNERS[draw1]:
            return f"{self.player1.name} wins with {draw1}"
        else:
            return f"{self.player2.name} wins with {draw2}"


if __name__ == "__main__":
    import maskpass

    game = RockPaperScissors()
    game.player1 = Player("Vasi")
    game.player2 = Player("Adrian")
    draw1 = maskpass.askpass("Vasi alege:").upper()
    draw2 = maskpass.askpass("Adrian alege:").upper()
    winner = game.play(draw1, draw2)
    print(winner)
