"""
This is my work for lab 6, a text adventure game. This work improves my understanding of classes, constructors, attributes, and lists.

https://learn.arcade.academy/en/latest/labs/lab_06_text_adventure/adventure.html#lab-06

Here is a map of the rooms.
###########
captain     blacksmith      living
treasure    snake           safe
###########
You start in the living room and you can navigate to other rooms. That's the whole game. 

08/22/2026
"""

from dataclasses import dataclass
@dataclass
class Room:
    """
    Class to describe one of 6 rooms.

    Describes the current room and which rooms touch it.

    Attributes
        description: describes the room
        north: the room number that appears directly north of this instance, or None if there is no room in the north.
        east: the room number that appears directly east of this instance, or None if there is no room in the east.
        south, west: same thing as north, but change "north" to "south" or "west", like in the east description.
    
    """
    description: str = ""
    north: int = 0
    east: int = 0
    south: int = 0
    west: int = 0

# save an explanation of how the game works.
help = "Inputs for navigation are NORTH, SOUTH, WEST, or EAST (N, S, W, or E as shorthands). \nType Q or QUIT to quit the game.\n Type H or HELP to see this message again. \nLetter case is irrelevant; upper-case and lower-case are treated as the same thing."

def main():
    """
    run the game.
    """
    # print the game explanation
    print(help)
    # create a list with 6 rooms. Each room is an instance of the Room class.
    room_list = []

    # Set the description and location of all 6 rooms. make room 0: living room. 
    room = Room(description="You are in the pirate ship's living room. The safe and blacksmith rooms point to the south and west, respectively."
                ,north=None
                ,south=5
                ,west=1
                ,east=None
                ) 
    room_list.append(room)

    # Make room 1: blacksmith room
    room = Room(description="You are in the blacksmith room! Get out of here! The blacksmith doesn't like vistitors. The living room, snake, and captain rooms point to the east, south, and west respectively."
            ,north=None
            ,south=4
            ,west=2
            ,east=0
            ) 
    room_list.append(room)

    # Make room 2: captains room.
    room = Room(description="You are in the captain's room! He is steering the ship right now. The blacksmith room points to the east, but its door is locked, so you can't use it. The treasure room points to the south."
                ,north=None
                ,south=3
                ,west=None
                ,east=None
                )
    room_list.append(room)

    # make room 3: treasure room.
    room = Room(description="Ta da! Here's the treasure room! There is a jar of coins on the floor. What did you expect? Captain-school is not cheap! The captain and snake room lie to the north and east, respectively."
                ,north=2
                ,south=None
                ,west=None
                ,east=4
                )
    room_list.append(room)

    # Make room 4: snake room.
    room = Room(description="Oh my god, it's a huge freaking snake. I'm not gonna let you interact with it because it's too scary. The captain thinks it's cool, so he's not gonna take it off. The blacksmith, treasure, and safe room lie in the north, west, and east, respectively."
                ,north=1
                ,south=None
                ,west=3
                ,east=5
                )
    room_list.append(room)
    # make room 5: safe room
    room = Room(description="You made it to the safe room! Congratulations. You can finally feel safe in this ship's 6 room cabin. All of those other rooms were soooooo scary! Actually, this was called the safe room because there used to be a safe here, but the blacksmith melted it down to craft a lock on his door; he doesn't want the captain to bother him, so he locked their door. The living room and snake room lie to the north and west, respectively."
                ,north=0
                ,south=None
                ,west=4
                ,east=None
                )
    room_list.append(room)

    # Allow the user to navigate between rooms.
    current_room = 0
    done = False

    while not done: # if the game is running, then ask where the user wants to go
        print("\n" + room_list[current_room].description)
        user_direction = input("Which direction do you want to go?")

        # if the user wants to go north, then change the current room to the north one.
        if user_direction.lower() == "n" or user_direction.lower() == "north":
            next_room = room_list[current_room].north
            # if the north room doesn't exist, then tell the user.
            if room_list[current_room].north == None:
                print("Sorry, matey! You can't go there")
            # if the north room exists, then move to the north room (that is, set the current room to the north room.)
            else: 
                current_room = next_room

        # repeat this block for every direction. South
        elif user_direction.lower() == "s" or user_direction.lower() == "south":
            next_room = room_list[current_room].south
            if room_list[current_room].south == None:
                print("Sorry, matey! You can't go there.")
            else: 
                current_room = next_room
        # West
        elif user_direction.lower() == "w" or user_direction.lower() == "west":
            next_room = room_list[current_room].west
            if room_list[current_room].west == None:
                print("Sorry, matey! You can't go there")
            else: 
                current_room = next_room
        # East
        elif user_direction.lower() == "e" or user_direction.lower() == "east":
            next_room = room_list[current_room].east

            if room_list[current_room].east == None:
                print("Sorry, matey! You can't go there")
            else: 
                current_room = next_room

        # if the user wants to quit, then stop the game.
        elif user_direction.lower() == "q" or user_direction.lower() == "quit":
            done=True
        elif user_direction.lower() == "h" or user_direction.lower() == "help":
            print(help)
        # if the user types something other than a direction or quit, then print the help statement.
        else:
            print("I don't understand you.")
main()

