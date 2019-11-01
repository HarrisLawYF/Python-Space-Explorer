# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:55:13 2019

@author: Harris
"""
from Robot import Robot

class Navigator(Robot):
    function = "navigation"
    __color = "white"
    
    def __init__(self, name, x, y, direction):
        # call super() function
        super().__init__(name, x, y, direction)
        self._print_slogan()
        print(self._wheel+1)
        
    def navigate(self):
        print("Putting navigation cone...")
        
    def get_color(self):
        return self.__color
        
    def reply(self, message = None):
        if message is not None:
            print("Self-service message: "+message)
        else:
            print("Aye aye sir")