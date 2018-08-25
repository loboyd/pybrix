"""Board class for pybrix

2018.08.20  --  L. Boyd"""

import pygame
import numpy as np

import display
from settings import GRID_SIZE, COLORS

class Board(object):
    def __init__(self, screen, shape=(20,10)):
        self.screen = screen
        self.shape = shape
        self.grid = -1*np.ones(self.shape, dtype=np.int8)

    def draw(self):
        """draw board not including currently falling tetromino"""
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                pos = (j+3, i)
                board_val = self.grid[i, j]
                color = COLORS[board_val]
                if board_val > -1:
                    display.draw_block(self.screen, pos, color)
                else:
                    gray = (64,64,64)  # gray border
                    display.draw_block(self.screen, pos, color, radius=0, border=gray, fancy=False)

    def clear_rows(self):
        """clears completed rows"""
        shift = 0  # no. of rows to move down
        for i in range(self.shape[0]-1, -1, -1):
            row = self.grid[i,:]
            # if row has 1+ empty space(s), shift down correct no. of rows
            if -1 not in row:
                shift += 1
            else:
                self.grid[i+shift,:] = row

        # fill in blank rows at the top
        self.grid[i:i+shift,:] = -1
        return int(shift)

