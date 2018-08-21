"""display functions for pybrix

2018.08.20  --  L. Boyd"""

import numpy as np
import pygame

from settings import GRID_SIZE, COLORS

def draw_block(screen, position, color):
    """draw single square to the screen"""
    row = GRID_SIZE*position[0]
    col = GRID_SIZE*position[1]
    white = (255,255,255)
    pygame.draw.rect(screen, white, pygame.Rect(row,col,40,40))
    pygame.draw.rect(screen, color, pygame.Rect(row+2,col+2,36,36))
