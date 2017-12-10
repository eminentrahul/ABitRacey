import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)

block_color = (34, 123, 203)

car_width = 73 



gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Bir Racey')
clock = pygame.time.Clock()

our_car = pygame.image.load('car.png')
#score board
def block_dodged(count):
    font = pygame.font.SysFont("Montserrat", 40)
    text = font.set_caption("Score:" +str(count), True, black)
    gameDisplay.blit(text, (0, 0))

#block
def block(block_x, block_y, block_w, block_h, color):
    pygame.draw.rect(gameDisplay, color, [block_x, block_y, block_w, block_h])

#car
def car(x, y):
    gameDisplay.blit(our_car, (x, y))


def text_object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont("Montserrat", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

def button(msg, x_pos, y_pos, btn_wid, btn_hgt, inactice_color, active_color, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if x_pos + btn_wid > mouse[0] > x_pos and y_pos + btn_hgt > mosue[1] > y:
        pygame.draw.rect(gameDisplay, active_color, ( x_pos, y_pos, btn_wid, btn_hgt))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, ( x_pos, y_pos, btn_wid, btn_hgt))
    smallText = pygame.font.SysFont("Montserrat", 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    textRect.center = ((x_pos + (btn_wid/2)), (y_pos + (btn_hgt/2)))
    gameDisplay.blit(textSurf, textSurf)

def quit_game():
    pygame.quit()
    quit()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("Montserrat", 115)
        TextSurf, TextRect = text_objects("A Bit Racey", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.bilt(TextSurf, TextRect)

        button("Go", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    block_start_x = random.randrange(0, display_width)
    block_start_y = -600
    block_speed = 4
    block_width = 100
    thing_height = 100

    blockCount = 1
    score = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
    x += x_change
    gameDisplay.fill(white)


    blocks(block_start_x, block_start_y, block_width,block_height, block_color)

    block_start_y += block_speed

    car(x, y)
    block_dodged(score)

    if x > display_width - car_width or x < 0:
        crash()

    if block_start_y > display_height:
        block_start_y = 0 - block_height
    
        
        

crashed = False
while not crashed:
    
 
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
