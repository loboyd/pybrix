"""Board class for pybrix

2018.08.20  --  L. Boyd"""

import pygame
import numpy as np

import display
from settings import GRID_SIZE, COLORS

class Board(object):
    def __init__(self, screen, shape=(22,10)):
        self.screen = screen
        self.shape = shape
        self.grid = -1*np.ones(self.shape, dtype=np.int8)

    def draw(self):
        """draw board not including currently falling tetromino"""
        for i in range(2,self.shape[0]):
            for j in range(self.shape[1]):
                pos = (j+3, i-2)
                board_val = self.grid[i, j]
                color = COLORS[board_val]
                #if board_val > -1:
                display.draw_block(self.screen, pos, color, border=True)

