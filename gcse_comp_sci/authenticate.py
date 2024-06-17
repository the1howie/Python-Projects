"""
Authenticate Users
Requirement: https://pypi.org/project/maskpass/
"""
import csv
from format_cmd import FormatCmdText
from constants import FORMAT_ON

try:
    import maskpass
    MASK_INSTALLED = True
except ModuleNotFoundError:
    MASK_INSTALLED = False

ABS_FILE_PATH = r"passwords.csv"


def read_users(file_path):
    users_list = []
    with open(file_path, "r") as f:
        users_file = csv.DictReader(f)
        for user in users_file:
            users_list.append(user)
    return users_list


def get_input(field_name):
    return str(input(f"\nEnter {field_name} (case sensitive): ")).strip()


def valid_username(username, users_list):
    for user in users_list:
        if user["username"] == username:
            return True
    return False


def prompt_username(users_list):
    attempts = 0
    username = get_input("user name")
    attempts += 1
    while not valid_username(username, users_list) and attempts < 3:
        print(f"Invalid input. Attempts left {3 - attempts}.")
        username = get_input("username")
        attempts += 1
    if attempts == 3:
        return None
    else:
        return username


def valid_password(username, password, users_list):
    for user in users_list:
        if user["username"] == username:
            if user["password"] == password:
                return True
    return False


def prompt_password(username, users_list):
    attempts = 0
    if MASK_INSTALLED:
        password = maskpass.askpass(mask="*")
    else:
        password = get_input("password")
    attempts += 1
    while not valid_password(username, password, users_list) and attempts < 3:
        print(f"Invalid input. Attempts left {3 - attempts}.")
        if MASK_INSTALLED:
            password = maskpass.askpass(mask="*")
        else:
            password = get_input("password")
        attempts += 1
    if attempts == 3:
        return None
    else:
        return password


def authenticate(users_list):
    fcmd = FormatCmdText(format_on=FORMAT_ON)
    username = prompt_username(users_list)
    if username is not None:
        password = prompt_password(username, users_list)
        if password is None:
            print(f"{fcmd.Red}Sorry {username}, ACCESS DENIED!{fcmd.Esc}")
            return None
    else:
        print("Invalid user name.")
        return None
    if username and password:
        print(f"{fcmd.Green}Good day {username}, access granted.{fcmd.Esc}")
        return {"username": username, "password": password}


if __name__ == "__main__":
    users_list = read_users(ABS_FILE_PATH)
    user = authenticate(users_list)
