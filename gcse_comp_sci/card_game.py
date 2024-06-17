"""Card Game"""
import os
import random
import copy
from enum import Enum
from format_cmd import FormatCmdText
from constants import FORMAT_ON
from utils import clear_console

GAME_NAME = "Card Game 🃏"

RANKS = [str(n) for n in range(1, 11)]

# I have replaced BLACK with BLUE such that I can format text.
class Suit(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3

BEATS = {
    Suit.RED: [Suit.BLUE],
    Suit.YELLOW: [Suit.RED],
    Suit.BLUE: [Suit.YELLOW]
}

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return f"Card(rank='{self.rank}', suit='{self.suit}')"
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    def __gt__(self, other):
        if self.suit == other.suit:
            return self.rank > other.rank
        else:
            return other.suit in BEATS[self.suit]

DECK = [Card(rank, suit) for rank in RANKS for suit in Suit]

CARD_TEMPLATE = (
    "┌───────┐",
    "│       │",
    "│  {} {}  │",
    "│       │",
    "└───────┘"
)

FORMAT_CARD = {
    Suit.RED: FormatCmdText(FORMAT_ON).Red,
    Suit.YELLOW: FormatCmdText(FORMAT_ON).Yellow,
    Suit.BLUE: FormatCmdText(FORMAT_ON).Blue
}

def print_card(card):
    print(FORMAT_CARD[card.suit], end="")
    for line in range(len(CARD_TEMPLATE)):
        if line == 2:
            rank = "T" if card.rank == "10" else card.rank
            print(CARD_TEMPLATE[line].format(card.suit.name[0], rank))
        else:
            print(CARD_TEMPLATE[line])
    print(FormatCmdText(FORMAT_ON).Esc)

def play_game(player1="Player 1", player2="Player 2"):
    fcmd = FormatCmdText(format_on=FORMAT_ON)
    clear_console()
    print(f"{GAME_NAME}")
    play_deck = copy.deepcopy(DECK)
    player1_wins = []
    player2_wins = []
    
    while len(play_deck) > 0:
        print(f"\n{fcmd.Yellow}Cards left in the deck {len(play_deck)}.{fcmd.Esc}")
        print(f"{fcmd.Green}{player1} score: {len(player1_wins)} \t{player2} score: {len(player2_wins)}{fcmd.Esc}")
        
        input(f"\n{player1}, pick a card (press ENTER)")
        card1 = random.choice(play_deck)
        play_deck.pop(play_deck.index(card1))
        print(f"{player1}, you have chosen:")
        print_card(card1)
        
        input(f"\n{player2}, pick a card (press ENTER)")
        card2 = random.choice(play_deck)
        play_deck.pop(play_deck.index(card2))
        print(f"{player2}, you have chosen:")
        print_card(card2)
        
        if card1 > card2:
            print(f"\n{player1} wins this round.")
            player1_wins.append(card1)
            player1_wins.append(card2)
        else:
            print(f"\n{player2} wins this round.")
            player2_wins.append(card1)
            player2_wins.append(card2)
    
    # Overall winner
    clear_console()
    print(fcmd.Red + "-" * 20 + " FINAL RESULT " + "-" * 20 + fcmd.Esc)
    print(f"{fcmd.Green}{player1} score: {len(player1_wins)} \t{player2} score: {len(player2_wins)}{fcmd.Esc}")
    if len(player1_wins) == len(player2_wins):
        print(f"\n{fcmd.Bold}It is a draw.{fcmd.Esc}\n")
    elif len(player1_wins) > len(player2_wins):
        print(f"\n{fcmd.Bold}{player1} wins!{fcmd.Esc}\n")
    else:
        print(f"\n{fcmd.Bold}{player2} wins!{fcmd.Esc}\n")


if __name__ == '__main__':
    play_game()
    # card = Card(rank=10, suit=Suit.RED)
    # print_card(card)
    