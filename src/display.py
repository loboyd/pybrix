"""display functions for pybrix

2018.08.20  --  L. Boyd"""

import numpy as np
import pygame

from settings import GRID_SIZE, COLORS, BOARD_SIZE

def draw_block_old(screen, position, color, border=False):
# def draw_block(screen, position, color, border=False):
    """draw single square to the screen"""
    s = GRID_SIZE
    row = s*position[0]
    col = s*position[1]
    white = (255,255,255)
    if border:
        pygame.draw.rect(screen, white, pygame.Rect(row,col,s,s))
        row += 2
        col += 2
        s -= 4
    pygame.draw.rect(screen, color, pygame.Rect(row,col,s,s))

def draw_block(screen, position, color, radius=0.3, interior=False, s=GRID_SIZE, border=None):
# def draw_fancy_block(screen, position, color, r, border=False):
    """draw single square with rounded corners (radius r) to the screen"""
    if radius < 0 or radius > 1:
        raise ValueError('radius must be between 0 and 1')

    color_tmp = (255,255,255)
    row = int(s*position[0])
    col = int(s*position[1])
    r = int(radius*s/4)  # maximum radius which doesn't go outside the square block
    for i in range(2):
        # draw the four corner circles
        pygame.draw.circle(screen, color_tmp, (row+r  ,col+r  ), r)
        pygame.draw.circle(screen, color_tmp, (row+r  ,col-r+s), r)
        pygame.draw.circle(screen, color_tmp, (row-r+s,col+r  ), r)
        pygame.draw.circle(screen, color_tmp, (row-r+s,col-r+s), r)

        # draw two rectangles to fill in
        pygame.draw.rect(screen, color_tmp, pygame.Rect(row,col+r,s,s-2*r))
        pygame.draw.rect(screen, color_tmp, pygame.Rect(row+r,col,s-2*r,s))

        # update settings for intertior color
        row += 1
        col += 1
        s -= 2
        color_tmp = color

    # draw highlight onto block surface
    # color_tmp = color_avg(color_tmp, (0,0,0))
    corner1 = (row+r,   col+r)
    corner2 = (row+r,   col-r+s)
    corner3 = (row-r+s, col-r+s)
    corner4 = (row-r+s, col+r)
    pygame.draw.line(screen, (  0,  0,  0), corner1, corner2)
    pygame.draw.line(screen, (  0,  0,  0), corner2, corner3)
    pygame.draw.line(screen, (255,255,255), corner3, corner4)
    pygame.draw.line(screen, (255,255,255), corner4, corner1)


def clear_screen(screen):
    """draw one huge black block over the screen
    NOTE: This function is probably no longer necessary"""
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
