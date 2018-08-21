"""Board class for pybrix

2018.08.20  --  L. Boyd"""

import pygame
import numpy as np

class Board(object):
    def __init__(self,shape=(20,10)):
        self.grid = np.array(shape)
