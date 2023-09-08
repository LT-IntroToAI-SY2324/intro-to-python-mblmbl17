# We will write a rock paper scissors game in class - Complete it in this file 
#Player and computer
#function to decide who wins, conditionals 
#Loop???
# we will need a dictionary
import random


def get_choices():
    options = ["rock", "paper", "scissors"]
    winner = 0
    while winner == 0:
        playerC = input("Enter your choice: ")
        computerC = random.choice(options)
        choices = {"player": playerC, "computer": computerC}
        if choices["player"] == "rock" and choices["computer"] == "rock":
            return "tie"
        if choices["player"] == "rock" and choices["computer"] == "scissors":
            return "player wins"
            winner += 1
        if choices["player"] == "rock" and choices["computer"] == "paper":
            return "computer wins"
            winner += 1
        if choices["player"] == "paper" and choices["computer"] == "paper":
            return "tie"
        if choices["player"] == "paper" and choices["computer"] == "rock":
            return "player wins"
            winner += 1
        if choices["player"] == "paper" and choices["computer"] == "scissors":
            return "computer wins"
            winner += 1
        if choices["player"] == "scissors" and choices["computer"] == "scissors":
            return "tie"
        if choices["player"] == "scissors" and choices["computer"] == "paper":
            return "player wins"
            winner += 1
        if choices["player"] == "scissors" and choices["computer"] == "rock":
            return "computer wins"
            winner += 1
    

choices = get_choices()
print(choices)