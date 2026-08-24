"""
practice using class methods. Instructions from:

https://learn.arcade.academy/en/latest/chapters/17_class_methods/class_methods.html#review-questions

08/23/2026
"""
#Create a class called Cat. Give it attributes for name, color, and weight. Give it a method called meow.
from dataclasses import dataclass
@dataclass
class Cat():
    name: str = ""
    color: str = ""
    weight: int = 0 # in kilograms
    def meow(self):
        print("meooooooww")

#Create an instance of the cat class, set the attributes, and call the meow method.
instance_of_cat_class = Cat()
instance_of_cat_class.name = "Eiffel"
instance_of_cat_class.color = "orange"
instance_of_cat_class.weight = 1.232e8

instance_of_cat_class.meow()

print(f"{instance_of_cat_class.name}'s weight is {instance_of_cat_class.weight} kilos")
#Create a class called Monster. Give it an attribute for name and an integer attribute for health. Create a method called decrease_health that takes in a parameter amount and decreases the health by that much. Inside that method, print that the animal died if health goes below zero.

@dataclass
class Monster():
    name: str = ""
    health: int = 100

    def decrease_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} is dead :(")

# test the Monster class
snake = Monster()
snake.name = "Mr. Snakey"
snake.decrease_health(119)
print(snake.health)