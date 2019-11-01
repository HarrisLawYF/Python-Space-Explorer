# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:55:24 2019

@author: Harris
"""
from Robot import Robot


class Fighter(Robot):
    function = "fighting"
    
    def __init__(self, name, x, y, direction):
        # call super() function
        super().__init__(name, x, y, direction)
        
    def fight(self):
        print("Shooting laser...")
        
    def reply(self, message = None):
        if message is not None:
            print("Self-service message: "+message)
        else:
            print("Yes sir!")