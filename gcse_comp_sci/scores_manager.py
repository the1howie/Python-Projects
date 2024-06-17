"""Update and print scores tables."""
import csv

from enum import IntEnum
from format_cmd import FormatCmdText
from constants import FORMAT_ON
from utils import clear_console
from operator import itemgetter

class Choice(IntEnum):
    finish = 0
    spock = 1
    music = 2
    dice = 3

CHOICES = [f"{c.name}[{c.value}]" for c in Choice]
CHOICES_STR = ", ".join(CHOICES)

SCORE_TEMPLATE = r"scores_{}.csv"

def read_scores(file_path):
    scores_list = []
    with open(file_path, "r") as f:
        scores_file = csv.DictReader(f)
        for score in scores_file:
            score['score'] = int(score['score'])
            scores_list.append(score)
    return scores_list

def print_table(data, headers=('username', 'score')):
    # instead of using tabulate module
    username_lengths = [len(x[headers[0]]) for x in data]
    username_lengths.append(len(headers[0]))
    max_len = max(username_lengths)
    border = "-" * max_len + "\t" + "-" * len(headers[1])
    
    print("\n" + border)
    print(f"{str(headers[0]).ljust(max_len)}\t{str(headers[1])}")
    print(border)
    
    for score_dict in data:
        print(f"{str(score_dict[headers[0]]).ljust(max_len)}\t{str(score_dict[headers[1]])}")
        
    print(border + "\n")

def print_leader_board(userchoice):
    fcmd = FormatCmdText(FORMAT_ON)
    file_name = SCORE_TEMPLATE.format(userchoice.name)
    scores_list = read_scores(file_name)
    clear_console()
    print(f"Leader Board for {fcmd.Yellow}{str(userchoice.name).capitalize()}{fcmd.Esc}:")
    
    if len(scores_list) > 1:
        scores_list.sort(key=itemgetter('score'), reverse=True)
    elif scores_list == []:
            scores_list.append({'username':'', 'score':''})
    print_table(scores_list)
       
def update_scores_list(username, points, userchoice):
    file_name = SCORE_TEMPLATE.format(userchoice.name)
    scores_list = read_scores(file_name)
    if scores_list == []:
        scores_list.append({'username': username, 'score': points})
    else:
        users = [score['username'] for score in scores_list]
        if username in users:
            for score in scores_list:
                if score['username'] == username:
                    score['score'] += points
                    break
        else:
            scores_list.append({'username': username, 'score': points})
    
    with open(file_name, 'w', newline='') as f:
        header =['username', 'score']
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for score in scores_list:
            writer.writerow(score)

def print_main(username="Guest"):
    fcmd = FormatCmdText(FORMAT_ON)
    clear_console()
    print(f"{fcmd.Green}Hello {username}{fcmd.Esc} 😊\n")
    print("\nSelect which leader board to view:\n")
    for ch in Choice:
        if ch is not Choice.finish:
            print(f"\t[{fcmd.Bold}{ch.value}{fcmd.Esc}] -- {ch.name}")
    print(f"\n{fcmd.Red}To quit, enter {fcmd.Bold}{Choice.finish.value}.{fcmd.Esc}")
    print("\n" + "-" * 73 + "\n")

def manage_leader_boards(username="Guest"):
    fcmd = FormatCmdText(FORMAT_ON)
    while True:
        print_main(username)
        try:
            value = input(f"\tEnter choice ({CHOICES_STR}): ")
            user_choice = Choice(int(value))
        except ValueError:
            print("Invalid choice!")
            continue
        
        if user_choice is not Choice.finish:
            clear_console()
            print_leader_board(user_choice)
            input(f"{fcmd.Grey}< Press ENTER to continue. >{fcmd.Esc}")      
        else:
            clear_console()
            break
    
    print(f"\n{fcmd.Yellow}Goodbye {username}.{fcmd.Esc}\n")

if __name__ == '__main__':
    # ch = Choice.music
    # username = 'JoeSoap'
    # points = 1
    # update_scores_list(username, points, ch)
    # print_leader_board(ch)
    manage_leader_boards()
