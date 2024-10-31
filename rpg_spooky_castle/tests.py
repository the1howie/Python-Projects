# from room import Room
# from character import Character, Enemy

# dave = Enemy("Dave", "A smelly zombie")
# dave.describe()

# dave.set_conversation("Hey, what's up dude?")
# dave.talk()

# dave.set_weakness("cheese")

# print("What will you fight with?")
# fight_with = input()
# dave.fight(fight_with)


# dave = Character("Dave", "A smelly zombie")
# dave.describe()

# dave.set_conversation("I eat human brains!")
# dave.talk()

# george = Character("George", "A villager")
# george.talk()


# kitchen = Room("Kitchen")
# kitchen.set_description("A dank and dirty room buzzing with flies.")

# dining_hall = Room("Dining Hall")
# dining_hall.set_description("A large room with ornate golden decorations on each wall.")

# ballroom = Room("Ballroom")
# ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

# kitchen.link_room(dining_hall, "south")
# dining_hall.link_room(kitchen, "north")
# dining_hall.link_room(ballroom, "west")
# ballroom.link_room(dining_hall, "east")

# current_room = kitchen

# while True:
#     print("\n")
#     current_room.get_details()
#     command = input("> ")
#     current_room = current_room.move(command)


# alive = True

# while alive:
#     print("\n")
#     current_room.get_details()
#     inhabitant = current_room.get_character()
#     command = input("> ")
#     if command in ["north", "south", "east", "west"]:
#         current_room = current_room.move(command)
#     elif command == "talk":
#         if inhabitant is not None:
#             inhabitant.talk()
#     elif command == "fight":
#         if inhabitant is not None:
#             print("What will you fight with?")
#             fight_with = input()
#             alive = inhabitant.fight(fight_with)
