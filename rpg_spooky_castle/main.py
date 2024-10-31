"""
This is the main file that runs the RPG.
"""

from room import Room
from character import Enemy, Friend
from rpginfo import RPGInfo
from item import Item

spooky_castle = RPGInfo("Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()

RPGInfo.author = "Raspberry Pi Foundation"
RPGInfo.credits()

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description(
    "A vast room with a shiny wooden floor. Huge candlesticks guard the entrance."
)

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

cheese = Item()
# cheese.name = "cheese"
# cheese.description = "Smelly and holly goodness"
cheese.set_name("cheese")
cheese.set_description("Smelly and holly goodness")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness(cheese)
dining_hall.set_character(dave)

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Why hello there.")
ballroom.set_character(catrina)

cornflakes = Item()
# cornflakes.name = "corn flakes"
# cornflakes.description = "Delicious golden flakes"
cornflakes.set_name("corn flakes")
cornflakes.set_description("Delicious golden flakes")

bob = Enemy("Bob", "Cereal killer")
bob.set_conversation("Meh... must... have... coco pops... skibbidi")
bob.set_weakness(cornflakes)
kitchen.set_character(bob)

kitchen.set_item(cheese)
dining_hall.set_item(cornflakes)

current_room = kitchen

backpack = []

def print_items(backpack):
    if backpack == []:
        print("Backpack is empty.")
    else:
        print("Backpack contains:") #, end=" ")
        for thing in backpack:
            #print(thing.name) #, end=", ")
            print(thing.get_name())
        print()

def use_item(backpack, look_for):
    for i, thing in enumerate(backpack):
        # if thing.name.lower() == look_for.lower():
        if thing.get_name().lower() == look_for.lower():
            return backpack.pop(i)
    else:
        return None

legal_commands = "north, south, east, west, talk, fight, take, hug, inventory, quit"

alive = True
finished_game = False
while alive and not finished_game:
    print("\n")
    current_room.get_details()
    print("[Legal commands: {}.]".format(legal_commands))

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item_found = current_room.get_item()
    if item_found is not None:
        item_found.describe()

    command = input("> ")

    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        # You can check whether an object is an instance of a particular
        # class with isinstance() - useful! This code means
        # "If the character is an Enemy"
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print_items(backpack)
            print("What will you fight with?")
            fight_with = input()
            combat_item = use_item(backpack, fight_with)

            if inhabitant.fight(combat_item):
                # What happens if you win?
                print("Hooray, you won the fight!")
                current_room.set_character(None)
                finished_game = Enemy.number_of_enemies == 0
            else:
                # What happens if you lose?
                print("Oh dear, you lost the fight.")
                print("That's the end of the game")
                alive = False
        else:
            print("There is no one here to fight with")

    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
        else:
            print("There is no one here to hug :(")

    elif command == "take":
        if isinstance(item_found, Item):
            backpack.append(current_room.get_item())
            current_room.set_item(None)
            print_items(backpack)
        else:
            print("There is nothing to take from here.")

    elif command == "inventory":
        print_items(backpack)

    elif command == "quit":
        alive = False
        print("We are sad to see you go...")

    else:
        print("Unknown command. Try again.")

if finished_game:
    print("\nYou have defeated all the enemies!")
