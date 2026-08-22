"""
This is my work for lab 6, a text adventure game. This work improves my understanding of classes, constructors, attributes, and lists.

https://learn.arcade.academy/en/latest/labs/lab_06_text_adventure/adventure.html#lab-06

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

        #def __post_init__(self):

def main():
    """
    ?
    """
    room_list = [] #why is room_list greyed out?

    # Make all 6 rooms. make room 0: nothing room. 
    room = Room(description="You are in the nothing room. There's nothing inside of the room. The safe and blacksmith point to the south and west, respectively."
                ,north=None
                ,south=5
                ,west=1
                ,east=None
                ) 
    room_list.append(room)
    # Make room 1: blacksmith room
    room = Room(description="You are in the blacksmith room! Get out of here! The blacksmith doesn't like vistitors. The nothing, snake, and necromancer rooms point to the east, south, and west respectively."
            ,north=None
            ,south=4
            ,west=2
            ,east=0
            ) 
    room_list.append(room)
    # Make room 2: necromancer room.
    room = Room(description="You are in the necromancer room! Oh wait. It's actually the soon-to-be-necromancer room; the necromancer failed his qualifying exams, last quarter. He studying necromancer books and plans on retaking his exams next quarter. Wish him luck! The blacksmith room points to the east, but its door is locked, so you can't use it. The treasure room points to the south."
                ,north=None
                ,south=3
                ,west=None
                ,east=None
                )
    room_list.append(room)
    # make room 3: treasure room.
    room = Room(description="Ta da! Here's the treasure room! Several pennies are glued to the floor. You can't pick them up. Haha. The necromancer and snake room lie to the north and east, respectively."
                ,north=2
                ,south=None
                ,west=None
                ,east=4
                )
    room_list.append(room)
    # Make room 4: snake room.
    room = Room(description="Oh my god, it's a huge freaking snake. I'm not gonna let you interact with it because it's too scary. The blacksmith, treasure, and safe room lie in the north, west, and east, respectively."
                ,north=None
                ,south=5
                ,west=1
                ,east=None
                )
    room_list.append(room)
    # make room 5: safe room
    room = Room(description="You made it to the safe room! Congratulations. You can now feel safe in this weird, rectangular building of 6 rooms. Actually, this was called the safe room because there used to be a safe here, but the blacksmith melted it down to craft a lock on his door; he doesn't want the necromancer to bother him, so he locked the door to necromancer. The nothing and snake room lie to the north and west, respectively."
                ,north=0
                ,south=None
                ,west=4
                ,east=None
                )
    room_list.append(room)

    # game loop.
    current_room = 0
    done = False
    while not done:
        print("\n" + room_list[current_room].description)
        user_direction = input("Which direction do you want to go?")
        if user_direction.lower() == "n" or user_direction.lower() == "north":
            print("nice")
        done = True ############## remove this in a bit later. Breaks the loop
main()

