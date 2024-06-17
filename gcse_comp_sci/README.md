Welcome!

This repo contains command line games only, that run with Python 3.

I have tried to write my own solutions to OCR's 2019 GCSE Computer Science projects.
See here: https://www.ocr.org.uk/Images/503195-programming-project-tasks-june-2019-and-june-2020.pdf

In addition, I have included the rock, paper, scissors, lizard, Spock games that I have learned how to code here: https://realpython.com/courses/python-rock-paper-scissors-game/

The games can be run individually, for example: `python dice_game.py`. My intention was, and still is for the players to run the `main_*.py` scripts to use as the main interaction with the games. 
* `python main_one_player.py`
* `python main_two_players.py`

For a more colourful experience, you can change `FORMAT_ON = True` in the `constants.py` file and this should work in Windows / DOS command prompts. You should see something like this:
![image](https://github.com/the1howie/Python-Projects/assets/32492300/972c1ea6-6072-4603-8942-10f4fc9fae9e)

And like so:
![image](https://github.com/the1howie/Python-Projects/assets/32492300/b86bc73a-5751-4f18-9e8c-b8aa6b4e2876)

Note that this has not been tested on Linux or Mac OS terminals. If you do run these scripts from an IDE, I would recommend https://code.visualstudio.com/. Other IDE's might not be able to process the colours in their terminal, and you should rather keep to `FORMAT_ON = False` in that case.

The data for the classic rock songs in `rock_songs.csv`, I sourced it from https://data.world/fivethirtyeight/classic-rock. I have trimmed the songs list down quite a bit.

You can make up your own usernames and passwords in the `passwords.csv`.

Enjoy!
