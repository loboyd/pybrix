#!/usr/bin/env python3
"""Main game logic for Pybrix

2018.08.23  --  GVG"""

import pygame
import sys
import os
import tetromino as tet
import display
from random import randint

from board import Board
from settings import GRID_SIZE, COLORS

def init():
    global f
    pygame.init()
    pygame.font.init()
    f = open("testing.out", "w")
    f.write("")

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
    state = enum('MENU','INIT','NEWPIECE','MOVEDOWN','MOTION','CLEARROWS')
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
    global level
    global b
    global upcoming_tets
    upcoming_tets = []
    textsurface = myfont.render('Init', False, (100, 100, 100),(0,0,255))
    screen.blit(textsurface,(0,0))
    # board = blank_board()
    # render_board(board,0)     # (no pieces yet)
    # score = 0
    # push_upcoming_piece() x3
    b = Board(screen)
    score = 0
    level = 1
    #for i in range(b.shape[0]):
    #    for j in range(b.shape[1]):
    #        b.grid[i, j] = sample([0,1,2,3,4,5,6],1)[0]
    b.draw()
    display.draw_score(screen, score)
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
    f.write("New tetromino, type " + str(s.shape) + "\n")
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
        if active_tet.check_lose():
            #render_loss_message()
            current_state = state.MENU
        else:
            current_state = state.CLEARROWS
            active_tet.add_to_board()
            b.draw()
    return;

def state_motion():     # Should respond to user instructions: translate, rotate, drop pieces
    global current_state
    global score
    global fall_speed
    global done
    textsurface = myfont.render('Motion', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    current_state = state.MOVEDOWN
    clk = pygame.time.get_ticks()
    a = 0
    dropped = 0
    while pygame.time.get_ticks() - clk < fall_speed and not dropped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                done = True
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            #    active_tet.translate(0)
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #    active_tet.translate(1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                active_tet.rotate(1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                active_tet.rotate(0)
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                active_tet.drop()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                t = active_tet.droppp()
                score+=t
                dropped = 1
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            f = open("testing.out","a")
            f.write("move left\n")
            if a:
                active_tet.translate(0)
                pygame.time.delay(200)
                a = 0
            else:
                a = 1
        if keys_pressed[pygame.K_RIGHT]:
            if a:
                active_tet.translate(1)
                pygame.time.delay(100)
                a = 0
            else:
                a = 1
        if keys_pressed[pygame.K_DOWN]:
            if a:
                active_tet.drop()
                pygame.time.delay(100)
                a = 0
            else:
                a = 1
        if keys_pressed[pygame.K_r]:
            if a:
                current_state = state.INIT
                pygame.time.delay(100)
                a = 0
            else:
                a = 1
        b.draw()
        active_tet.draw()
        pygame.display.flip()
        keys_pressed = pygame.key.get_pressed()
        display.draw_score(screen, score)
        level = int(score/1000)+1
        display.draw_level(screen, level)
        fall_speed = 200 + 800/level
    return;

def state_clearrows():      # Clear filled rows and drop bulk accordingly
    rowscores = [0, 40, 100, 300, 1200]
    global current_state
    global score
    textsurface = myfont.render('Clear Rows', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    numrows = b.clear_rows()
    current_state = state.NEWPIECE
    score += rowscores[numrows]*(level+1)
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
        state.CLEARROWS: state_clearrows,
    }
    func = switcher.get(argument, lambda: "nothing")
    return func()

main()
