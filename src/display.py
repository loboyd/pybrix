"""display functions for pybrix

2018.08.20  --  L. Boyd"""

import numpy as np
import pygame

from settings import GRID_SIZE, COLORS, BOARD_SIZE

def draw_block(screen, position, color):
    """draw single square to the screen"""
    row = GRID_SIZE*position[0]
    col = GRID_SIZE*position[1]
    s = GRID_SIZE
    white = (255,255,255)
    pygame.draw.rect(screen, white, pygame.Rect(row,col,s,s))
    pygame.draw.rect(screen, color, pygame.Rect(row+2,col+2,36,36))

def clear_screen(screen):
    """draw one huge black block over the screen"""
    black = (0,0,0)
    height = GRID_SIZE*BOARD_SIZE[0]
    width = GRID_SIZE*BOARD_SIZE[1]

    pygame.draw.rect(screen, black, pygame.Rect(0,0,width,height))

