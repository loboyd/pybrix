"""display functions for pybrix

2018.08.20  --  L. Boyd"""

import numpy as np
import pygame

from settings import GRID_SIZE, COLORS, BOARD_SIZE

def draw_block(screen, position, color, border=False):
    """draw single square to the screen"""
    row = GRID_SIZE*position[0]
    col = GRID_SIZE*position[1]
    s = GRID_SIZE
    white = (255,255,255)
    if border:
        pygame.draw.rect(screen, white, pygame.Rect(row,col,s,s))
        row += 2
        col += 2
        s -= 4
    pygame.draw.rect(screen, color, pygame.Rect(row,col,s,s))

def clear_screen(screen):
    """draw one huge black block over the screen"""
    black = (0,0,0)
    height = GRID_SIZE*BOARD_SIZE[0]
    width = GRID_SIZE*BOARD_SIZE[1]

    pygame.draw.rect(screen, black, pygame.Rect(0,0,width,height))

def draw_score(screen, score, border=False):
    white = (255,255,255)
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    pygame.draw.rect(screen, white, pygame.Rect(5, GRID_SIZE*BOARD_SIZE[0]+10, 7*GRID_SIZE, 2*GRID_SIZE))
    textsurface = myfont.render("Score:  " + str(score), False, (100, 100, 100),(255,255,255))
    screen.blit(textsurface,(5,GRID_SIZE*BOARD_SIZE[0]+30))

def draw_level(screen, level, border=False):
    white = (255,255,255)
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    pygame.draw.rect(screen, white, pygame.Rect(5, GRID_SIZE*BOARD_SIZE[0]+110, 7*GRID_SIZE, 2*GRID_SIZE))
    textsurface = myfont.render("Level:  " + str(level), False, (100, 100, 100),(255,255,255))
    screen.blit(textsurface,(5,GRID_SIZE*BOARD_SIZE[0]+130))
