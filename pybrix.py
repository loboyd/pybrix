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
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    screen = pygame.display.set_mode((600, 600))
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


def state_menu():
    global current_state
    textsurface = myfont.render('Menu', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    current_state+=1
    return;

def state_init():
    global current_state
    textsurface = myfont.render('Init', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    current_state+=1
    return;

def state_newpiece():
    global current_state
    textsurface = myfont.render('New Piece', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    current_state+=1
    return;

def state_movedown():
    global current_state
    textsurface = myfont.render('Move Down', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    current_state+=1
    return;

def state_motion():
    global current_state
    textsurface = myfont.render('Motion', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    current_state+=1
    return;

def state_checksitting():
    global current_state
    textsurface = myfont.render('Check Sitting', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    current_state+=1
    return;

def state_checklose():
    global current_state
    textsurface = myfont.render('Check Lose', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    current_state+=1
    return;

def state_clearrows():
    global current_state
    textsurface = myfont.render('Clear Rows', False, (0, 0, 0),(0,0,255))
    screen.blit(textsurface,(0,0))
    current_state=0
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
