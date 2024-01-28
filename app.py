import random

CHOICES = ["Rock", "Paper", "Scissors"]


class Player:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.choice = self.draw()

    @staticmethod
    def draw():
        return random.choice(CHOICES)


class Game:
    @staticmethod
    def decide_winner(player1, player2):
        if player1.choice == player2.choice:
            return "Tie"
        elif player1.choice == "Rock":
            if player2.choice == "Paper":
                return f"{player2.name} {player2.surname} Wins"
            else:
                return f"{player1.name} {player1.surname} Wins"
        elif player1.choice == "Paper":
            if player2.choice == "Scissors":
                return f"{player2.name} {player2.surname} Wins"
            else:
                return f"{player1.name} {player1.surname} Wins"
        elif player1.choice == "Scissors":
            if player2.choice == "Rock":
                return f"{player2.name} {player2.surname} Wins"
            else:
                return f"{player1.name} {player1.surname} Wins"


if __name__ == "__main__":
    player1 = Player("Simon", "Vasile")
    player2 = Player("Adrian", "Moloce")

    game = Game()
    draw = game.decide_winner(player1, player2)

    while draw == "Tie":
        player1 = Player("Simon", "Vasile")
        player2 = Player("Adrian", "Moloce")
        draw = game.decide_winner(player1, player2)

    print(draw)
