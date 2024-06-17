"""
This script manages all the solitaire games, prints the menu, and runs the require modules.
"""
import authenticate
import Spock
import music_quiz
import dice_game

from enum import IntEnum
from format_cmd import FormatCmdText
from constants import FORMAT_ON
from utils import clear_console
from scores_manager import update_scores_list, print_leader_board

class Choice(IntEnum):
    finish = 0
    spock = 1
    music = 2
    dice = 3

CHOICES = [f"{c.name}[{c.value}]" for c in Choice]
CHOICES_STR = ", ".join(CHOICES)

GAME_NAMES = {
    Choice.finish: "Quit",
    Choice.spock: Spock.GAME_NAME,
    Choice.music: music_quiz.GAME_NAME,
    Choice.dice: dice_game.GAME_NAME,
}

RUN_GAMES = {
    Choice.finish: {"module": None, "function": ""},
    Choice.spock: {"module": Spock, "function": "play_game"},
    Choice.music: {"module": music_quiz, "function": "play_quiz"},
    Choice.dice: {"module": dice_game, "function": "play_game"},
}

ABS_FILE_PATH = r"passwords.csv"
    
# authentificate
def auth(path):
    users_list = authenticate.read_users(path)
    return authenticate.authenticate(users_list)

# main menu
def print_main(username="Guest"):
    fcmd = FormatCmdText(format_on=FORMAT_ON)
    clear_console()
    print(f"{fcmd.Green}Hello {username}{fcmd.Esc} 😊\n")
    
    for ch in Choice:
        if ch is not Choice.finish:
            print(f"\t[{fcmd.Bold}{ch.value}{fcmd.Esc}] -- {GAME_NAMES[ch]}")
    print(f"\n{fcmd.Red}To quit, enter {fcmd.Bold}{Choice.finish.value}.{fcmd.Esc}")
    print("\n" + "-" * 73 + "\n")
    

def validate_choice(user_choice):
    try:
        game = RUN_GAMES[user_choice]
        return getattr(game["module"], game["function"])
    except Exception as e:
        print(e)
        return None

# manage everything
def manager(username):
    fcmd = FormatCmdText(format_on=FORMAT_ON)
    while True:
        print_main(username)
        try:
            value = input(f"\tEnter choice ({CHOICES_STR}): ")
            user_choice = Choice(int(value))
        except ValueError:
            print("Invalid choice!")
            continue
        
        # check here which game to play
        if user_choice is not Choice.finish:
            clear_console()
            play_func = validate_choice(user_choice)
            points = play_func() # call the appropriate function
            input(f"{fcmd.Grey}< Press ENTER to continue. >{fcmd.Esc}") # wait for key press 
            if username != "Guest":
                update_scores_list(username, points, user_choice)
                print_leader_board(user_choice)
                input(f"{fcmd.Grey}< Press ENTER to continue. >{fcmd.Esc}") # wait for key press         
        else:
            clear_console()
            break
    
    print(f"\n{fcmd.Yellow}Goodbye {username}.{fcmd.Esc}\n")


if __name__ == '__main__':
    fcmd = FormatCmdText(format_on=FORMAT_ON)
    clear_console()
    print("Welcome!")
    print("-" * 8)
    
    username = ""
    sign_in = input("\nSign in (Y/n)? ").strip()
    if len(sign_in) > 0 and sign_in[0].lower() == "n":
        username = "Guest"
        print(f"\n{fcmd.Green}Welcome Guest{fcmd.Esc}👋")
        input(f"{fcmd.Grey}Press ENTER to continue.{fcmd.Esc}") # wait for key press
        
    else:
        user = auth(ABS_FILE_PATH) # authorize user
        if user is not None:
            username = user["username"]
        else:
            print(f"\n{fcmd.Blue}Better luck next time.{fcmd.Esc}\n")
    
    if username != "":
        manager(username)
    