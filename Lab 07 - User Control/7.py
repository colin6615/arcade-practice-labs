""" Lab 7 - User Control 
https://learn.arcade.academy/en/latest/labs/lab_07_user_control/user_control.html

- use arrow keys to move the sun
- Use mouse to move the snowman
- Sound plays if you 
    - right click
    - or try to move the sun off of the screen

- The snowman and sun drawings are from the textbook examples.
"""

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 10

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
    """ draw grass at fixed coordinates. """
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


class Moving_snow_person:
    """ Make a moving snow person that the user can move around with their mouse. """
    def __init__(self, position_x, position_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y

    def draw(self):
        """ Draw the moving snow person with the instance variables we have. """
        draw_snow_person(x=self.position_x, 
                         y=self.position_y)

class Moving_sun:
    """ The user can move this sun with their keyboard. """

    def __init__(self, position_x, position_y, change_x, change_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = 100

        # load sound and make sound-playing attribute 
        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
        self.explosion_sound_player = None # if sound is not playing, then this thing is None.



    def draw(self):
        """ Draw the sun with the instance variables we have. """
        draw_sun(self.position_x, self.position_y)
    def update(self):
        # load laser sound. I think its from the Kenney website, https://kenney.nl/
        # but idk. the instructions just gave me this file and they didn't tell me where it came from.
        self.laser_sound = arcade.load_sound("laser.wav")

        # Move the sun
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the sun hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius
            # play explosion sound if sound is not already playing. This way, arcade doesn't play the explosion sound 60 times per second. Instead, arcade plays one explosion sound at a time.
            if not self.explosion_sound_player or not self.explosion_sound_player.playing:
                self.explosion_sound_player = arcade.play_sound(self.explosion_sound)


        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            if not self.explosion_sound_player or not self.explosion_sound_player.playing:
                self.explosion_sound_player = arcade.play_sound(self.explosion_sound)



        if self.position_y < self.radius:
            self.position_y = self.radius
            if not self.explosion_sound_player or not self.explosion_sound_player.playing:
                self.explosion_sound_player = arcade.play_sound(self.explosion_sound)



        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            if not self.explosion_sound_player or not self.explosion_sound_player.playing:
                self.explosion_sound_player = arcade.play_sound(self.explosion_sound)



class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        
        # Load the sound when the application starts
        self.laser_sound = arcade.load_sound("laser.wav")

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Create our moving snow dude & sun
        self.moving_snow_person_instance = Moving_snow_person(50, 50)
        self.moving_sun = Moving_sun(300,300, 0,0)

    def on_draw(self):
        self.clear()

        # draw the background
        arcade.set_background_color(arcade.color.DARK_BLUE)
        draw_grass()

        # draw the moving stuff
        self.moving_snow_person_instance.draw()
        self.moving_sun.draw()


    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.moving_snow_person_instance.position_x = x
        self.moving_snow_person_instance.position_y = y

    def on_update(self, delta_time):
        self.moving_sun.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.moving_sun.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.moving_sun.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.moving_sun.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.moving_sun.change_y = -MOVEMENT_SPEED


    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.laser_sound)


    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.moving_sun.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.moving_sun.change_y = 0
def main():
    window = MyGame()
    arcade.run()


main()