"""Tetromino class for pybrix

2018.08.19  --  L. Boyd"""

import numpy as np
import pygame

import display
from settings import GRID_SIZE, COLORS

# other blocks relative to `position` block
BLOCKS = [
    ((-1., 0.), (0.,0.), ( 1., 0.), (2., 0.)), # 1x4
    ((-1., 0.), (0.,0.), ( 0.,-1.), (1.,-1.)), # S
    ((-1.,-1.), (0.,0.), ( 0.,-1.), (1., 0.)), # S'
    ((-1., 0.), (0.,0.), ( 1., 0.), (1.,-1.)), # L
    ((-1., 0.), (0.,0.), (-1.,-1.), (1., 0.)), # L'
    ((-1., 0.), (0.,0.), ( 0.,-1.), (1., 0.)), # T
    (( 0.,-1.), (0.,0.), ( 1.,-1.), (1., 0.)), # square
]
# make vector from above into numpy arrays
for i in range(len(BLOCKS)):
    blocks = BLOCKS[i]
    BLOCKS[i] = tuple([np.array(i) for i in blocks])

# translation from position reference block to rotational center
ROTATION_POINT = [
    np.array((0.5, 0.5)),
    np.array((0.0, 0.0)),
    np.array((0.0, 0.0)),
    np.array((0.0, 0.0)),
    np.array((0.0, 0.0)),
    np.array((0.0, 0.0)),
    np.array((0.5,-0.5)),
]


class Tetromino(object):
    def __init__(self, shape, board, screen, orientation=0, position=(5,-1)):
        self.shape = shape
        self.board = board
        self.screen = screen
        self.orientation = orientation
        self.position = position
        self.board_collision = False
        self.is_drawn = False

    def drop(self):
        """advance tetromino by one row
        TODO: include check for hitting existing Tetrominos"""
        self.undraw()
        self.position = (self.position[0], self.position[1]+1)
        # check for board collisions
        self.check_board_collision()
        # undo drop if found
        if self.board_collision:
            self.position = (self.position[0], self.position[1]-1)
            self.board_collision = False
            return False
        return True

    def droppp(self):
        """advance tetromino by all rows"""
        self.undraw()
        n = 0
        while 1:
            self.position = (self.position[0], self.position[1]+1)
            # check for board collisions
            self.check_board_collision()
            # undo drop if found
            if self.board_collision:
                self.position = (self.position[0], self.position[1]-1)
                self.board_collision = False
                return n
            n+=1

    def get_block_positions(self):
        """returns a list of all board locations used by a tetromino
        NOT COMPLETED"""
        blocks = BLOCKS[self.shape]

        # translate so rotational center and position reference
        # are the same
        blocks = [i - ROTATION_POINT[self.shape] for i in blocks]

        # rotate blocks to correct orientation
        blocks = rotate_blocks(blocks, self.orientation)

        # undo translation from above
        blocks = [i + ROTATION_POINT[self.shape] for i in blocks]

        return [self.position + i for i in blocks]

    def translate(self, direction=1):
        """TODO: perform boundary check"""
        self.undraw()
        t = 1 if direction else -1
        self.position = (self.position[0]+t, self.position[1])
        # check for board collisions
        self.check_board_collision()
        # if found, undo translation
        if self.board_collision:
            self.position = (self.position[0]-t, self.position[1])
            self.board_collision = False
            return False
        return True

    def rotate(self,ccw=False):
        self.undraw()
        t = -1 if ccw else 1
        self.orientation = (self.orientation+t) % 4
        self.check_board_collision()
        if self.board_collision:
            self.orientation = (self.orientation-t) % 4
            self.board_collision = False
            return False
        return True

    def draw(self):
        blocks = self.get_block_positions()
        color = COLORS[self.shape]
        for block in blocks:
            display.draw_block(self.screen, block, color, border=True)
        self.is_drawn = True

    def undraw(self):
        if self.is_drawn:
            blocks = self.get_block_positions()
            for block in blocks:
                display.draw_block(self.screen, block, (0,0,0))
            self.is_drawn = False

    def check_board_collision(self):
        blocks = self.get_block_positions()
        for block in blocks:
            u,v = map(int,block)
            ushift = 3  
            if u < ushift or u >= (self.board.shape[1]+ushift):
                self.board_collision = True
            elif v >= self.board.shape[0]:
                self.board_collision = True
            elif v>=0 and self.board.grid[v,u-ushift] != -1:
                self.board_collision = True
        if self.board_collision:
            f = open("testing.out","a")
            f.write("Collision at " + str(u) + ", " + str(v) + "\n")
        return self.board_collision

    def add_to_board(self):
        blocks = self.get_block_positions()
        ushift = 3
        for block in blocks:
            u,v = map(int,block)
            self.board.grid[v,u-ushift] = self.shape
            f = open("testing.out","a")
            f.write("Added to board at " + str(u) + ", " + str(v) + "\n")
        return;

    def check_lose(self):
        blocks = self.get_block_positions()
        for block in blocks:
            u,v = map(int,block)
            if v<0:
                return True
        return False;
            


def rotate_blocks(blocks,r):
    """rotates a set of points in 2D space by r*90 degrees"""
    r = r % 4
    if r == 0:
        return blocks

    for i in range(len(blocks)):
        block = blocks[i]
        if r == 1:
            blocks[i] = (-block[1], block[0])
        elif r == 2:
            blocks[i] = (-block[0], -block[1])
        elif r == 3:
            blocks[i] = (block[1],-block[0])
    return blocks
