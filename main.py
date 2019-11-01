# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:34:48 2019

@author: Harris
"""

# https://stackabuse.com/object-oriented-programming-in-python/
# https://www.programiz.com/python-programming/multiple-inheritance
from Navigator import Navigator
from Fighter import Fighter
from Tokota import Tokota
from Direction import Direction
from Robot import Robot

def set_movement(movement, robot, map):
    if(movement == "L"):
        robot.turn_left()
    elif(movement == "R"):
        robot.turn_right()
    else:
        robot.move_forward(map)


print (Robot.get_bot_secret()[0])
print (Robot.get_bot_secret()[1])

map = {'x': 5, 'y': 5}
map_x = int(input("Map x coordinate: ")) 
map_y = int(input("Map y coordinate: "))

map['x'] = map_x
map['y'] = map_y

nav_bot_name = str(input("Nav bot name: "))
nav_bot_x = int(input("Nav bot x coordinate: "))
nav_bot_y = int(input("Nav bot y coordinate: "))
nav_bot_dir = str(input("Nav bot direction: "))
nav_bot_inst = str(input("Nav bot movement: "))

fight_bot_name = str(input("Fight bot name: "))
fight_bot_x = int(input("Fight bot x coordinate: "))
fight_bot_y = int(input("Fight bot y coordinate: "))
fight_bot_dir = str(input("Fight bot direction: "))
fight_bot_inst = str(input("Fight bot movement: "))

nav_bot = Navigator(nav_bot_name, nav_bot_x, nav_bot_y, Direction[nav_bot_dir])
for m in [char for char in nav_bot_inst]:
    nav_bot.navigate()
    set_movement(m, nav_bot, map)
nav_bot.reply("I am robot")

fight_bot = Fighter(fight_bot_name, fight_bot_x, fight_bot_y, Direction[fight_bot_dir])
for m in [char for char in fight_bot_inst]:
    fight_bot.fight()
    set_movement(m, fight_bot, map)
fight_bot.reply()

tokota_bot = Tokota("XT009", 0, 0, Direction.N)

print(nav_bot.get_x())
print(nav_bot.get_y())
print(nav_bot.get_direction())
print(nav_bot.__class__.function)
print(nav_bot.get_color())
print('-------------------------')
print(fight_bot.get_x())
print(fight_bot.get_y())
print(fight_bot.get_direction())
print(fight_bot.__class__.function)