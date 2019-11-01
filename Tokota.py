# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 23:47:39 2019

@author: Harris
"""
from Direction import Direction
from Navigator import Navigator

class Tokota(Navigator):
    def __init__(self, name, x, y, direction):
        # call super() function
        super().__init__(name, x, y, direction)
        self._print_slogan()
        print(self._wheel+1)