# Melissa Pallay
# Exercise 1.7 - Rock, Paper, Scissors
# 2/2/14

"""
Table:
Player 1 | Player 2 | Result

Rock     | Rock     | Tie
Rock     | Paper    | Player 2
Rock     | Scissors | Player 1
Paper    | Rock     | Player 1
Paper    | Paper    | Tie
Paper    | Scissors | Player 2
Scissors | Rock     | Player 2
Scissors | Paper    | Player 1
Scissors | Scissors | Tie
"""

list = ['rock', 'paper', 'scissors']
player1 = raw_input("Player 1? ")
while player1 not in list:
    print "This is not a valid object selection. Try again!"
    player1 = raw_input("Player 1? ")

player2 = raw_input("Player 2? ")
while player2 not in list:
    print "This is not a valid object selection. Try again!"
    player2 = raw_input("Player 2? ")

if player1 == player2:
    winner = "It's a Tie"

if (player1 == 'rock' and player2 == 'paper') or (player1 == 'paper' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'rock'):
    winner = 'Player 2 wins'

if (player1 == 'rock' and player2 == 'scissors') or (player1 == 'paper' and player2 == 'rock') or (player1 == 'scissors' and player2 == 'paper'):
    winner = 'Player 1 wins'

print winner
