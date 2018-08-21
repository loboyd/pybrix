#!/usr/bin/env python3
"""Test the board.draw() method
This test should draw a board with a single 1x4 tetromino at the bottom.
2018.08.20  --  L. Boyd"""

import pygame
import sys
import os

# add src to path before import pybrix stuff
cwd = os.getcwd()[:-4]
print(cwd)
sys.path.insert(0, cwd)
sys.path.insert(0, cwd+'/src')

from src.board import Board
from src.settings import GRID_SIZE, COLORS

b = Board()

# place a Tetromino
b.grid[19,4] = 1
b.grid[18,4] = 1
b.grid[17,4] = 1
b.grid[16,4] = 1

pygame.init()
screen = pygame.display.set_mode((10*GRID_SIZE, 20*GRID_SIZE))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
