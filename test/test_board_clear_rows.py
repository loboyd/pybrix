#!/usr/bin/env python3
"""Test the board.clear_rows() method
The test should draw a board with three rows (two filled) and
then clear them two seconds later.
2018.08.23  --  L. Boyd"""

import pygame
import sys
import os
import time
from random import sample

# add src to path before import pybrix stuff
cwd = os.getcwd()[:-4]
print(cwd)
sys.path.insert(0, cwd)
sys.path.insert(0, cwd+'/src')

from src.board import Board
from src.settings import GRID_SIZE, COLORS

pygame.init()
screen = pygame.display.set_mode((15*GRID_SIZE, 30*GRID_SIZE))

b = Board(screen)

# place a Tetromino
# b.grid[19,4] = 0
# b.grid[18,4] = 0
# b.grid[17,4] = 0
# b.grid[16,4] = 0

for i in range(b.shape[0]-3, b.shape[0]):
    for j in range(b.shape[1]):
        if (i, j) != (b.shape[0]-2, 5):
            b.grid[i, j] = sample([0,1,2,3,4,5,6],1)[0]

b.draw()
t1 = time.time()

done = False
while not done:
    if time.time() > t1 + 0.5:
        b.clear_rows()
        b.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
