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
    def __init__(self, shape, board, orientation=0, position=(0,5)):
        self.shape = shape
        self.board = board
        self.orientation = orientation
        self.position = position
        self.board_collision = False

    def drop(self):
        """advance tetromino by one row
        TODO: include check for hitting existing Tetrominos"""
        self.position = (self.position[0], self.position[1]+1)
        # check for board collisions
        # undo drop if found
        if self.board_collsision:
            self.position = (self.position[0], self.position[1]-1)
            return False
        return True

    def get_block_positions(self):
        """returns a list of all board locations used by a tetromino
        NOT COMPLETED"""
        blocks = BLOCKS[self.shape]

        # translate so rotational center and position reference
        # are the same
        blocks = [i + ROTATION_POINT[self.shape] for i in blocks]

        # rotate blocks to correct orientation
        blocks = rotate_blocks(blocks, self.orientation)

        # undo translation from above
        blocks = [i - ROTATION_POINT[self.shape] for i in blocks]

        return [self.position + i for i in blocks]

    def translate(self, direction=1):
        """TODO: perform boundary check"""
        t = 1 if direction else -1
        self.position = (self.position[0]+t, self.position[1])
        # check for board collisions
        # if found, undo translation
        if self.board_collision:
            self.position = (self.position[0]-t, self.position[1])
            return False
        return True

    def rotate(self,ccw=False):
        t = -1 if ccw else 1
        self.orientation = (self.oreintation+t) % 4

    def draw(self, screen):
        blocks = self.get_block_positions()
        for block in blocks:
            display.draw_block(screen, block, COLORS[self.shape])

    def check_board_collision(self):
        blocks = self.get_block_positions
        for block in blocks:
            u,v = block
            if u < 0 or u > self.board.shape[0]:
                self.board_collision = True
            elif v < 0 or u > self.board.shape[1]:
                self.board_collision = True
            elif self.board[u,v] != -1:
                self.board_collision = True
        return board_collision


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
            blocks[i] = (-block[0], block[1])
        elif r == 3:
            blocks[i] = (block[1],-block[0])
    return blocks
