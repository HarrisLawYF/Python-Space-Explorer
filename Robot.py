# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:54:19 2019

@author: Harris
"""
from Direction import Direction
from abc import ABC, abstractmethod    

# ABC is an abstract class kind of metaclass
class Robot(ABC):
    # class attribute can be shared by child classes, it is like a static variable
    cardinal = dict([(0, Direction.N),(1, Direction.E),(2, Direction.S),(3, Direction.W),(-1, Direction.W),(-2, Direction.S),(-3, Direction.E)])
    _wheel = 4
    
    def __init__(self, name, x, y, direction):
        self.name = name
        # variable with __ is private variable
        # variable with _ is private variable
        self._x = x
        self._y = y
        self._direction = direction
        
    @abstractmethod
    def reply(self, message=None):
        pass
    
    def _print_slogan(self):
        print("Robot reports for duty")
    
    def get_direction(self):
        return self._direction
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def turn_left(self):
        dir_value = (list(Robot.cardinal.keys())[list(Robot.cardinal.values()).index(self._direction)])
        dir_value = (dir_value - 1) % 4
        self._direction = Robot.cardinal.get(dir_value)
    
    def turn_right(self):
        dir_value = (list(Robot.cardinal.keys())[list(Robot.cardinal.values()).index(self._direction)])
        dir_value = (dir_value + 1) % 4
        self._direction = Robot.cardinal.get(dir_value)
    
    def __move_up(self, map):
        if(self._y < map.get('y')):
            self._y+=1
            
    def __move_right(self, map):
        if(self._x < map.get('x')):
            self._x+=1
            
    def __move_down(self):
        if(self._y > 0):
            self._y-=1
            
    def __move_left(self):
        if(self._x > 0):
            self._x-=1
            
    @staticmethod
    def get_bot_secret():
        return "S1","S2"
    
    def move_forward(self, map):
        if(self._direction == Direction.N):
            self.__move_up(map)
        elif(self._direction == Direction.E):
            self.__move_right(map)
        elif(self._direction == Direction.S):
            self.__move_down()
        else:
            self.__move_left()