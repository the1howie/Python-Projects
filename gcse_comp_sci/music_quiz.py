""" Music Quiz """
import random
import csv
from format_cmd import FormatCmdText
from constants import FORMAT_ON

GAME_NAME = "Music Quiz"
DATA_PATH = r"rock_songs.csv"
MAX_ATTEMPTS = 2

def read_songs(file_path):
    songs_list = []
    with open(file_path, "r") as f:
        songs_file = csv.DictReader(f)
        for song in songs_file:
            songs_list.append(song)
    return songs_list

def check_answer(guess, computer_choice):
    return guess.lower() == computer_choice["song"].lower()

def mask_name(name):
    # return " ".join([word[0] + "*" * (len(word) - 1) for word in name.split()])
    chars = ["(", ")", "'", "/", "-", "_", ",", ".", "?", "!", ":", ";", "&", "#"]
    words = name.split()
    mask = []
    for word in words:
        masked_word = ""
        for pos, letter in enumerate(word):
            if pos == 0:
                masked_word += letter
            elif len(word) > 1 and pos == 1:
                if word[0] in chars:
                    masked_word += letter
                else:
                    masked_word += "*"
            elif letter in chars:
                masked_word += letter
            else:
                masked_word += "*"
        mask.append(masked_word)
    return " ".join(mask)

def match_guesses(attempts, computer_choice):
    guess = input(f"   Enter guess ({attempts} attempts left): ")
    match_song = check_answer(guess, computer_choice)
    if not match_song:
        attempts -= 1
        while attempts > 0 and not match_song:
            guess = input(f"   Enter guess ({attempts} attempts left): ")
            match_song = check_answer(guess, computer_choice)
            if not match_song:
                attempts -= 1
    return (match_song, attempts)

def play_quiz():
    fcmd = FormatCmdText(format_on=FORMAT_ON)
    songs = read_songs(DATA_PATH)
    points = 0
    questions = 0
    correct = 0
    print("Welcome to the Music Quiz 🎸🎵")

    while True:
        computer_choice = random.choice(songs)
        artist_name = computer_choice["artist"].capitalize()
        song_name = computer_choice["song"]
        song_masked = mask_name(song_name)
        attempts = MAX_ATTEMPTS
        print(f'\nGuess the song name "{song_masked}" by the artist "{artist_name}"?')
        match_song = match_guesses(attempts, computer_choice)
        
        if match_song[0]:
            print(f'{fcmd.Green}You guessed correctly! 🤩 Yes, it was "{song_name}" by "{artist_name}".{fcmd.Esc}')
            if match_song[1] == MAX_ATTEMPTS:
                points += 3
            else:
                points += 1
            correct += 1
        else:
            print(f'{fcmd.Red}Sorry, incorrect. 😪 It was "{song_name}" by "{artist_name}".{fcmd.Esc}')
        questions += 1
        
        print(f"\nTotal Points: {points}")
        again = input("\n    Play again? (Y/n): ").strip()
        if len(again) > 0 and again[0].lower() == "n":
            break

    print(f'\n{fcmd.Yellow}You got {correct} out of {questions} questions correct with a total of {points} points.{fcmd.Esc} 😎')
    print("\nGoodbye!\n")
    
    return points


if __name__ == '__main__':
    import os
    os.system("cls" if os.name == "nt" else "clear")
    play_quiz()
