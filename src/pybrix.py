"""Main game logic for Pybrix

2018.08.20  --  GVG"""

import pygame
import sys
import os
import tetromino as tet
from random import randint

# add src to path before import pybrix stuff
cwd = os.getcwd()[:-4]
print(cwd)
sys.path.insert(0, cwd)
sys.path.insert(0, cwd+'/src')

from src.board import Board
from src.settings import GRID_SIZE, COLORS


def init():
    global f
    pygame.init()
    pygame.font.init()
    f = open("testing.out", "w")
    #f.write("123")

def main():
    init()
    global myfont
    global screen
    global state
    global current_state
    global clock
    global done
    global score
    global upcoming_tets
    global fall_speed
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    screen = pygame.display.set_mode((600, 1000))
    clock = pygame.time.Clock()
    done = False
    state = enum('MENU','INIT','NEWPIECE','MOVEDOWN','MOTION','CHECKLOSE','CLEARROWS')
    current_state = state.MENU
    score = 0
    upcoming_tets = []
    fall_speed = 1000
    while not done:
        screen.fill((100, 100, 100))
        state_execute(current_state)             
        pygame.display.flip()
        #screen.fill((0, 0, 0))


def state_menu():   # Should display main menu and check for input on menu options
    global current_state
    textsurface = myfont.render('Menu', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    # render_menu()
    # 
    for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                        done = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                current_state+=1
    return;

def state_init():   # Should start game: display empty board, reset score, show first pieces
    global current_state
    global score
    global b
    textsurface = myfont.render('Init', False, (100, 100, 100),(0,0,255))
    screen.blit(textsurface,(0,0))
    # board = blank_board()
    # render_board(board,0)     # (no pieces yet)
    # score = 0
    # push_upcoming_piece() x3
    b = Board(screen)
    score = 0

    #for i in range(b.shape[0]):
    #    for j in range(b.shape[1]):
    #        b.grid[i, j] = sample([0,1,2,3,4,5,6],1)[0]
    b.draw()
    push_upcoming_tet(upcoming_tets, b, screen)
    push_upcoming_tet(upcoming_tets, b, screen)
    push_upcoming_tet(upcoming_tets, b, screen)
    current_state+=1
    return;

def push_upcoming_tet(upcoming_tets, board, screen):
    r = randint(0,6)
    upcoming_tets.append(tet.Tetromino(r, board, screen))
    return r;

def state_newpiece():   # Should place random new piece above top row of board, and cycle coming pieces
    global current_state
    global active_tet
    textsurface = myfont.render('New Piece', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    active_tet = pop_upcoming_tet(upcoming_tets)
    push_upcoming_tet(upcoming_tets, b, screen)
    b.draw()
    active_tet.draw()
    current_state+=1
    return;

def pop_upcoming_tet(upcoming_tets):
    f = open("testing.out","a")
    s = upcoming_tets.pop(0)
    f.write("\n"+str(s.shape))
    return s;

def state_movedown():   # Should move active piece down one row
    global current_state
    textsurface = myfont.render('Move Down', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    if active_tet.drop():
        b.draw()
        active_tet.draw()
        current_state+=1
    else:
        current_state = state.NEWPIECE
        active_tet.add_to_board()
        b.draw()
    return;

def state_motion():     # Should respond to user instructions: translate, rotate, drop pieces
    global current_state
    textsurface = myfont.render('Motion', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    current_state = state.MOVEDOWN
    clk = pygame.time.get_ticks()
    while pygame.time.get_ticks() - clk < fall_speed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                done = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                active_tet.translate(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                active_tet.translate(1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                active_tet.rotate(1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                active_tet.rotate(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                active_tet.drop()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                active_tet.droppp()
                #current_state = state.CLEARROWS
            b.draw()
            active_tet.draw()
            pygame.display.flip()
    return;

def state_checklose():      # Should check if active piece rested above top (and top row not full)
    global current_state
    textsurface = myfont.render('Check Lose', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    # if active_piece.checkLose() and !(board.rowFull(board.nrows-1)):
    #   display_loss_message()
    #   current_state = state_MENU
    # else:
    #   current_state = state_CLEARROWS
    current_state+=1
    return;

def state_clearrows():      # Clear filled rows and drop bulk accordingly
    global current_state
    textsurface = myfont.render('Clear Rows', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    # for x in range(0, board.nrows):
    #   if board.rowFull(x):
    #       board.clearRow(x)
    #   else:   x+=1
    # current_state = state_NEWPIECE
    current_state += 1    
    return;

def enum(*args):
    enums = dict(zip(args, range(len(args))))
    return type('Enum', (), enums)

def state_execute(argument):
    switcher = {
        state.MENU: state_menu,
        state.INIT: state_init,
        state.NEWPIECE: state_newpiece,
        state.MOVEDOWN: state_movedown,
        state.MOTION: state_motion,
        state.CHECKLOSE: state_checklose,
        state.CLEARROWS: state_clearrows, 
    }
    func = switcher.get(argument, lambda: "nothing")
    return func()

main()
