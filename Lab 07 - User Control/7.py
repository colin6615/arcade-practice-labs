""" Lab 7 - User Control 
https://learn.arcade.academy/en/latest/labs/lab_07_user_control/user_control.html

"""

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# --- Create functions to draw stuff ----
def draw_sun(x,y):
    arcade.draw_circle_filled(x, y, 40, arcade.color.YELLOW)

    # Rays to the left, right, up, and down. 
    arcade.draw_line(x, y, x-100, y, arcade.color.YELLOW, 3)
    arcade.draw_line(x, y, x+100, y, arcade.color.YELLOW, 3)
    arcade.draw_line(x, y, x, y-100, arcade.color.YELLOW, 3)
    arcade.draw_line(x, y, x, y+100, arcade.color.YELLOW, 3)

    # Diagonal rays
    arcade.draw_line(x, y, x+50, y+50, arcade.color.YELLOW, 3)
    arcade.draw_line(x, y, x+50, y-50, arcade.color.YELLOW, 3)
    arcade.draw_line(x, y, x-50, y+50, arcade.color.YELLOW, 3)
    arcade.draw_line(x, y, x-50, y-50, arcade.color.YELLOW, 3)

def draw_grass():
    """ Draw the ground """
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 3, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)

# Make a moving snow person that the user can move around.
class Moving_snow_person:
    def __init__(self, position_x, position_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y

    def draw(self):
        """ Draw the moving snow person with the instance variables we have. """
        draw_snow_person(x=self.position_x, 
                         y=self.position_y)
        # arcade.draw_circle_filled(self.position_x,
        #                          self.position_y,
        #                          self.radius,
        #                          self.color)



class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Create our moving dude
        self.moving_snow_person_instance = Moving_snow_person(50, 50)

    def on_draw(self):
        self.clear()

        # draw the background
        arcade.set_background_color(arcade.color.DARK_BLUE)
        draw_grass()
        draw_snow_person(150, 140)
        draw_snow_person(450, 180)
        draw_sun(230,300)

        # draw the moving stuff
        self.moving_snow_person_instance.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.moving_snow_person_instance.position_x = x
        self.moving_snow_person_instance.position_y = y



def main():
    window = MyGame()
    arcade.run()


main()