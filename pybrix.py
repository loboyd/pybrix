import pygame
def init():
    pygame.init()
    pygame.font.init() 

def main():
    init()
    global myfont
    global screen
    global state
    global current_state
    global clock
    global done
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    done = False
    state = enum('MENU','INIT','NEWPIECE','MOVEDOWN','MOTION','CHECKSITTING','CHECKLOSE','CLEARROWS')
    current_state = state.MENU
    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                        done = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        screen.fill((0, 0, 0))
                        state_execute(current_state)            

            
            pygame.display.flip()
            #screen.fill((0, 0, 0))


def state_menu():   # Should display main menu and check for input on menu options
    global current_state
    textsurface = myfont.render('Menu', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    # render_menu()
    # 
    current_state+=1
    return;

def state_init():   # Should start game: display empty board, reset score, show first pieces
    global current_state
    textsurface = myfont.render('Init', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    # board = blank_board()
    # render_board(board,0)     # (no pieces yet)
    # score = 0
    # push_upcoming_piece() x3
    current_state+=1
    return;

def state_newpiece():   # Should place random new piece above top row of board, and cycle coming pieces
    global current_state
    textsurface = myfont.render('New Piece', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    # active_piece = pull_upcoming_piece()
    # push_upcoming_piece()
    current_state+=1
    return;

def state_movedown():   # Should move active piece down one row
    global current_state
    textsurface = myfont.render('Move Down', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    # active_piece.position(2) -= 1     # (y position)
    # render_board(board,active_piece)
    current_state+=1
    return;

def state_motion():     # Should respond to user instructions: translate, rotate, drop pieces
    global current_state
    textsurface = myfont.render('Motion', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    current_state+=1
    # clock.tick()
    # while clock.tick() < fall_speed:
    #   for event in pygame.event.get():
    #                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
    #                    done = True
    #                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
    #                    active_piece.translate(1)
    #                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
    #                    active_piece.translate(0)
    #                elif event.type == pygame.KEYDOWN and event.key == pygame.K_z:
    #                    active_piece.rotate(1)
    #                elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
    #                    active_piece.rotate(0)
    #                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    #                    active_piece.fall()
    #                    current_state = state_CLEARROWS
    return;

def state_checksitting():   # Should check if active piece is resting on bulk 
    global current_state
    textsurface = myfont.render('Check Sitting', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    # if active_piece.checkSitting():
    #   current_state = state_CHECKLOSE
    # else:
    #   current_state = state_MOVEDOWN
    current_state+=1
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
        state.CHECKSITTING: state_checksitting,
        state.CHECKLOSE: state_checklose,
        state.CLEARROWS: state_clearrows, 
    }
    func = switcher.get(argument, lambda: "nothing")
    return func()

main()
