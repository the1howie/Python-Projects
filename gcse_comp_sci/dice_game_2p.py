""" Two-player dice game """
from enum import IntEnum
from dice_game import throw_dice, calc_points, print_dice, print_nums
from format_cmd import FormatCmdText
from constants import FORMAT_ON
from utils import clear_console

GAME_NAME = "Two-player Dice Game 🎲🎲"

class Result(IntEnum):
    loss = 0
    draw = 1
    win = 2

def result(score1, score2, player1, player2):
    if score1 == score2:
        return decider(player1, player2)
    elif score1 > score2:
        return Result.win
    else:
        return Result.loss

def roll_dice():
    throws = throw_dice()
    print_nums(throws)
    print_dice(throws)
    return calc_points(throws)

def decider(player1, player2):
    throw1 = [1]
    throw2 = [1]
    fcmd = FormatCmdText(FORMAT_ON)
    
    print("\nThe Decider!")
    while throw1 == throw2:
        input(f"\n 🎲 {fcmd.Blue}{player1}, throw again (press ENTER){fcmd.Esc}")
        throw1 = throw_dice(1)
        print_nums(throw1)
        print_dice(throw1)
        
        input(f"\n 🎲 {fcmd.Red}{player2}, throw again (press ENTER){fcmd.Esc}")
        throw2 = throw_dice(1)
        print_nums(throw2)
        print_dice(throw2)
    
    return Result.win if throw1 > throw2 else Result.loss
    
    
def run_two_player_game(player1="Player 1", player2="PLayer 2"):
    # track two scores
    rolls = 1
    score1 = 0
    score2 = 0
    fcmd = FormatCmdText(FORMAT_ON)

    while rolls < 6:
        clear_console()
        print(f"{fcmd.Yellow}{GAME_NAME}{fcmd.Esc}")
        print(f"{fcmd.Blue}{fcmd.Italics}{player1}:{fcmd.Esc} {score1} vs {fcmd.Red}{fcmd.Italics}{player2}:{fcmd.Esc} {score2}")
        print("-" * 40)
        print(f"\n{fcmd.Bold}Roll {rolls}{fcmd.Esc}")
        
        input(f"🎲 {fcmd.Blue}{player1}, roll the dice (press ENTER)!{fcmd.Esc}") 
        points = roll_dice()
        print(f"\t{player1}, roll {rolls} points: {points}")
        score1 += points
        
        print()
        input(f"🎲 {fcmd.Red}{player2}, roll the dice (press ENTER)!{fcmd.Esc}") 
        points = roll_dice()
        print(f"\t{player2}, roll {rolls} points: {points}")
        score2 += points
        
        print("-" * 40)
        print(f"\n{fcmd.Bold}Roll {rolls}{fcmd.Esc}")
        print(f"\t{player1} total: {score1}")
        print(f"\t{player2} total: {score2}")
        print("-" * 40)
        rolls += 1
        input() # wait for key press
     
    player1_result = result(score1=score1, score2=score2, player1=player1, player2=player2)
    winner = player1 if player1_result == Result.win else player2
    
    clear_console()
    print(f"{fcmd.Yellow}{GAME_NAME}{fcmd.Esc}")
    print(f"{fcmd.Blue}{fcmd.Italics}{player1}:{fcmd.Esc} {score1} vs {fcmd.Red}{fcmd.Italics}{player2}:{fcmd.Esc} {score2}")
    print("-" * 40)
    print(f"\n{fcmd.Green}{fcmd.Bold}And the winner is {winner}!{fcmd.Esc}")
    print(f"\nWell played! 👏\n")


if __name__ == '__main__':
    # Play as guests.
    run_two_player_game()
    