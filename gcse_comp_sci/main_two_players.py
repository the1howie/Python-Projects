""" This script manages all the two-player games."""
import authenticate
import card_game
import dice_game_2p

from enum import IntEnum
from format_cmd import FormatCmdText
from constants import FORMAT_ON
from utils import clear_console

class Choice(IntEnum):
    finish = 0
    cards = 1
    dice = 2

CHOICES = [f"{c.name}[{c.value}]" for c in Choice]
CHOICES_STR = ", ".join(CHOICES)

GAME_NAMES = {
    Choice.finish: "Quit",
    Choice.cards: card_game.GAME_NAME,
    Choice.dice: dice_game_2p.GAME_NAME,
}

RUN_GAMES = {
    Choice.finish: {"module": None, "function": ""},
    Choice.cards: {"module": card_game, "function": "play_game"},
    Choice.dice: {"module": dice_game_2p, "function": "run_two_player_game"},
}

ABS_FILE_PATH = r"passwords.csv"
    
# authentificate
def auth(path):
    users_list = authenticate.read_users(path)
    return authenticate.authenticate(users_list)

# main menu
def print_main(player1="Guest1", player2="Guest2"):
    fcmd = FormatCmdText(format_on=FORMAT_ON)
    clear_console()
    print(f"{fcmd.Green}Hello {player1} and {player2}{fcmd.Esc} 😊\n")
    
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
def manager(player1, player2):
    fcmd = FormatCmdText(format_on=FORMAT_ON)
    while True:
        print_main(player1=player1, player2=player2)
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
            play_func(player1=player1, player2=player2) # call the appropriate function
            input(f"{fcmd.Grey}< Press ENTER to continue. >{fcmd.Esc}") # wait for key press         
        else:
            clear_console()
            break
    
    print(f"\n{fcmd.Yellow}Goodbye {player1} and {player2}.{fcmd.Esc}\n")

if __name__ == '__main__':
    fcmd = FormatCmdText(format_on=FORMAT_ON)
    clear_console()
    print("Welcome!")
    print("-" * 8)
    sign_in = input("\nSign in (Y/n)? ").strip()
    if len(sign_in) > 0 and sign_in[0].lower() == "n":
        player1 = "Guest1"
        player2 = "Guest2"
        print(f"\n{fcmd.Green}Welcome Guest{fcmd.Esc}👋")
        input(f"{fcmd.Grey}Press ENTER to continue.{fcmd.Esc}") # wait for key press
        manager(player1=player1, player2=player2)
    else:
        print(f"\n{fcmd.Grey}Log-in for Player 1{fcmd.Esc}")
        user1 = auth(ABS_FILE_PATH) # authorize user
        if user1 is not None:
            print(f"\n{fcmd.Grey}Log-in for Player 2{fcmd.Esc}")
            user2 = auth(ABS_FILE_PATH) # authorize user
            if user2 is not None:
                player1 = user1["username"]
                player2 = user2["username"]
                manager(player1=player1, player2=player2)
            else:
                print(f"\n{fcmd.Blue}Better luck next time.{fcmd.Esc}\n")
        else:
            print(f"\n{fcmd.Blue}Better luck next time.{fcmd.Esc}\n")
