# Imagine working on software for a game of Rock, Paper, Scissors

# Create a function named `winner` that takes two arguments,
# the move for player_1 and player_2 ("rock", "paper", or "scissors"),
# and returns the winner ("Player 1 wins!", "Player 2 wins!", or "It's a tie").

from enum import Enum
import re

class Move(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    def __str__(self):
        return self.value

    @staticmethod
    def sanitize_string(s):
        sanitized_move = re.sub(r"[^a-zA-Z]", "", s).upper()

        try:
            return Move[sanitized_move]
        except KeyError:
            raise ValueError(f"Invalid move, '{s}'. Choose 'rock', 'paper', or 'scissors'.")

    def beats(self, other):
        return (self == Move.ROCK and other == Move.SCISSORS) or \
        (self == Move.SCISSORS and other == Move.PAPER) or \
        (self == Move.PAPER and other == Move.ROCK)

def winner(player_1, player_2):
    try:
        player_1_move = Move.sanitize_string(player_1)
        player_2_move = Move.sanitize_string(player_2)
    except ValueError as e:
        raise ValueError(e)

    if player_1_move == player_2_move:
        return "It's a tie!"
    elif player_1_move.beats(player_2_move):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

print(winner("rock", "paper")) # Player 2 wins!
print(winner("scissors", "paper")) # Player 1 wins!
print(winner("scissors", "rock")) # Player 2 wins!

print(winner("PAper", "rOck")) # Player 1 wins!
print(winner("paper123", "rock5")) # Player 1 wins!
print(winner("paper!!", "rock%")) # Player 1 wins!

print(winner("lizards", "rock")) # ValueError
print(winner("[]", "rock")) # ValueError
