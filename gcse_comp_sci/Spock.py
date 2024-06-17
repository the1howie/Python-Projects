""" 
Rock, Paper, Scissors, Lizard, Spock (5-Way game) 
Source: https://realpython.com/courses/python-rock-paper-scissors-game/
"""

import random
from enum import IntEnum
from format_cmd import FormatCmdText
from constants import FORMAT_ON

GAME_NAME = "Rock, paper, scissors, lizard, Spock"

class Choice(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


CHOICES = [f"{c.name}[{c.value}]" for c in Choice]
CHOICES_STR = ", ".join(CHOICES)

BEATS = {
    Choice.Rock: [Choice.Lizard, Choice.Scissors, ],
    Choice.Paper: [Choice.Spock, Choice.Rock, ],
    Choice.Scissors: [Choice.Lizard, Choice.Paper, ],
    Choice.Lizard: [Choice.Spock, Choice.Paper, ],
    Choice.Spock: [Choice.Scissors, Choice.Rock, ],
}

MESSAGES = {
    (Choice.Rock, Choice.Scissors): "crushes",
    (Choice.Rock, Choice.Lizard): "crushes",
    (Choice.Paper, Choice.Rock): "covers",
    (Choice.Paper, Choice.Spock): "disproves",
    (Choice.Scissors, Choice.Paper): "cut",
    (Choice.Scissors, Choice.Lizard): "decapitates",
    (Choice.Lizard, Choice.Paper): "eats",
    (Choice.Lizard, Choice.Spock): "poisons",
    (Choice.Spock, Choice.Scissors): "smashes",
    (Choice.Spock, Choice.Rock): "vaporizes",
}

FORMAT_CMD = {
    Choice.Rock: FormatCmdText(FORMAT_ON).Grey,
    Choice.Paper: FormatCmdText(FORMAT_ON).Cyan,
    Choice.Scissors: FormatCmdText(FORMAT_ON).Red,
    Choice.Lizard: FormatCmdText(FORMAT_ON).Green,
    Choice.Spock: FormatCmdText(FORMAT_ON).Yellow,
}

SYMBOLS = {
    Choice.Rock: "🪨 ",
    Choice.Paper: "📃 ",
    Choice.Scissors: "✂️ ",
    Choice.Lizard: "🦎 ",
    Choice.Spock: "🖖 ",
}


class Outcome(IntEnum):
    Loss = 0
    Tie = 1
    Win = 2


def show_winner(user_choice, computer_choice):
    fcmd = FormatCmdText(format_on=FORMAT_ON)
    if user_choice == computer_choice:
        print(f"It's a tie! Both users chose " + 
              f"{FORMAT_CMD[user_choice]}{user_choice.name}{fcmd.Esc} {SYMBOLS[user_choice]}.")
        return Outcome.Tie
    else:
        # BEATS[user_choice] is the list of things that user_choice wins over
        user_wins = computer_choice in BEATS[user_choice]

        if user_wins:
            verb = MESSAGES[(user_choice, computer_choice)]
            print(f"{FORMAT_CMD[user_choice]}{user_choice.name}{fcmd.Esc} {SYMBOLS[user_choice]} {verb}" + 
                  f" {FORMAT_CMD[computer_choice]}{computer_choice.name}{fcmd.Esc} {SYMBOLS[computer_choice]}," + 
                  f" {fcmd.Bold}you win!{fcmd.Esc}")
            return Outcome.Win
        else:
            verb = MESSAGES[(computer_choice, user_choice)]
            print(f"{FORMAT_CMD[computer_choice]}{computer_choice.name}{fcmd.Esc} {SYMBOLS[computer_choice]} {verb}" + 
                  f" {FORMAT_CMD[user_choice]}{user_choice.name}{fcmd.Esc} {SYMBOLS[user_choice]}," + 
                  f" {fcmd.Underline}you lose!{fcmd.Esc}")
            return Outcome.Loss

def play_game():
    games = 0
    wins = 0
    ties = 0
    fcmd = FormatCmdText(format_on=FORMAT_ON)
    print(f"{fcmd.Bold}Welcome to {fcmd.Esc}🪨  📃 ✂️  🦎 🖖\n")
    
    while True:
        print("\nMake your throw")
        try:
            value = input(f"    Enter a choice ({CHOICES_STR}): ")
            user_choice = Choice(int(value))
        except ValueError:
            print(f"\nYou typed {value} which isn't a valid choice!")
            continue

        games += 1
        value = random.randint(0, len(Choice) - 1)
        computer_choice = Choice(value)
        result = show_winner(user_choice, computer_choice)
        if result == Outcome.Win:
            wins +=1
        elif result == Outcome.Tie:
            ties +=1

        again = input(f"\n{fcmd.Grey}Play again? (Press ENTER or Y/n): {fcmd.Esc}").strip()
        if len(again) > 0 and again[0].lower() == "n":
            break

    print(f"\nYou got {fcmd.Green}{wins} wins{fcmd.Esc}, " + 
          f"{fcmd.Yellow}{ties} ties{fcmd.Esc} and " + 
          f"{fcmd.Red}{games - wins - ties} losses{fcmd.Esc} in {games} games. 😎")
    print("\nGoodbye!\n")
    
    return wins * Outcome.Win.value + ties * Outcome.Tie.value


if __name__ == '__main__':
    import os
    os.system("cls" if os.name == "nt" else "clear")
    play_game()
