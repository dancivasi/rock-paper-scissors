import random


choices = ["Rock", "Paper", "Scissors"]
class Player():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def draw(self):
        return random.choice(choices)


