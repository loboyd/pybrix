"""Board class for pybrix

2018.08.20  --  L. Boyd"""

import pygame
import numpy as np

import display
from settings import GRID_SIZE, COLORS

class Board(object):
    def __init__(self,shape=(20,10)):
        self.shape = shape
        self.grid = np.array(self.shape)

    def draw(self, screen):
        """draw board not including currently falling tetromino"""
        for i in self.shape[0]:
            for j in self.shape[1]:
                position = ()
                color = COLORS[self.grid[i,j]]
                display.draw_block(screen, position, color)

