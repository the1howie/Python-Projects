"""
One-player / solitaire dice game. 

Dice art source: https://youtu.be/x-Ag2_bJ40Y?si=OoGQru33p-sXi0KS

To obtain the Unicodes for 6-sided die, run this: 
print('\u2680 \u2681 \u2682 \u2683 \u2684 \u2685')
⚀ ⚁ ⚂ ⚃ ⚄ ⚅
SIDES = '⚀⚁⚂⚃⚄⚅' # it works, but too small to read!

To build unicode art for bigger dice, run this: 
print('\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518')
● ┌ ─ ┐ │ └ ┘
rather build a dictionary for the dice art.
"""
import random
from format_cmd import FormatCmdText
from constants import FORMAT_ON
from utils import clear_console

GAME_NAME = "Solitaire Dice Game 🎲🎲"

DICE_ART = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    2: ("┌─────────┐", 
        "│ ●       │", 
        "│         │", 
        "│       ● │", 
        "└─────────┘"),
    3: ("┌─────────┐", 
        "│ ●       │", 
        "│    ●    │", 
        "│       ● │", 
        "└─────────┘"),
    4: ("┌─────────┐", 
        "│ ●     ● │", 
        "│         │", 
        "│ ●     ● │", 
        "└─────────┘"),
    5: ("┌─────────┐", 
        "│ ●     ● │", 
        "│    ●    │",
        "│ ●     ● │", 
        "└─────────┘"),
    6: ("┌─────────┐", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "└─────────┘")
}

def throw_dice(n=2):
    # throw two dice by default
    throws = [random.randint(1, 6) for _ in range(n)]
    return throws

def print_dice(throws):
    for line in range(5):
        for throw in throws:
            print(DICE_ART[throw][line], end=" ")
        print()
    print()
    
def print_nums(throws):
    nums = ", ".join(map(str, throws))
    print(f"You have rolled: {nums}")

def calc_points(throws):
    points = sum(throws)
    if points % 2 == 0:
        points += 10
    else:
        points = max(0, points - 5)
    
    if len(throws) == 2 and throws[0] == throws[1]:
        input('You rolled a double. You get an extra throw. Press ENTER!')
        extra = throw_dice(1)
        print_dice(extra)
        points += extra[0]
    
    return points

def play_game():
    rolls = 0
    total = 0
    fcmd = FormatCmdText(format_on=FORMAT_ON)
    
    clear_console()
    print(f"{fcmd.Yellow}{GAME_NAME}{fcmd.Esc}")
    print(f"Running total: {total}")
    print("-" * 22)
    # wait for key press
    input(f"🎲 {fcmd.Blue}Throw the dice (press ENTER)!{fcmd.Esc}") 
    
    while True:
        rolls += 1
        clear_console()
        print(f"{fcmd.Yellow}{GAME_NAME}{fcmd.Esc}")
        print(f"Running total: {total}")
        print
        print("-" * 22)
        throws = throw_dice()
        print_nums(throws)
        print_dice(throws)
        
        points = calc_points(throws)
        print(f"Points for this roll: {points}")
        total += points
        
        print("-" * 22)
        print(f"Running total: {total}")
        print("-" * 22)
        
        # wait for key press
        again = input(f"🎲 {fcmd.Blue}Throw again? (press ENTER or type N to quit): {fcmd.Esc}").strip()
        if again.lower() == "n":
            break
    
    clear_console()
    print("-" * 22)
    print(f"{fcmd.Yellow}{GAME_NAME}{fcmd.Esc}")
    print(f"\nNumber of rolls 🎲🎲: {rolls}")
    print(f"{fcmd.Green}You earned a total of {total} points{fcmd.Esc}.\n")
    print("-" * 22)
    print("\nWell done! 👏\n")
    
    return total
    

if __name__ == '__main__':
    play_game()
    