import pygame
from random import randint
import time


class Jerry():

    def __init__(self):
        pass

    def blit(self):
        pass

pygame.init()

clock = pygame.time.Clock()

surfaceWidth = 1065
surfaceHeight = 743

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))

pygame.display.set_caption('Tom and Jerry Chase')

jerry_stand = pygame.image.load('jerry_stand.png').convert_alpha()
jerry_stand_width = 50
jerry_stand_height = 64
kitchen = pygame.image.load('kitchen.png').convert_alpha()
jerry_run_right = pygame.image.load('jerry_run_right.png').convert_alpha()
jerry_run_left = pygame.image.load('jerry_run_left.png').convert_alpha()
plate = pygame.image.load('plate_small.png').convert_alpha()
broken_plate = pygame.image.load('broken_plate.png').convert_alpha()

plate_rect = plate.get_rect()
jerry_stand_rect = jerry_stand.get_rect()

jerry_x = jerry_stand_rect.x
jerry_y = jerry_stand_rect.y

plate_width = plate.get_width()
plate_height = plate.get_height()


def score(count, broken_plates):
    font = pygame.font.Font('freesansbold.ttf', 20)
    score = font.render('Score: ' + str(count), True, (255, 255, 0))
    broken = font.render('Broken Plates: ' + str(broken_plates), True, (0, 255, 0))
    surface.blit(score, [0, 0])
    surface.blit(broken, [surfaceWidth - broken.get_width(), 0])


def blit_plate(img, x, y):
    surface.blit(img, (x, y))


def blit_jerry(img, x, y):
    surface.blit(img, (x, y))

jerry_stand_rect.x = 50
jerry_stand_rect.y = 640
jerry_move = 0

plate_rect.x = randint(0, surface.get_width() - plate.get_width())
plate_rect.y = 0 - plate.get_height()
plate_move = 0
pause = 0

current_score = 0
broken_plates = 0

game = True

while game:

    # print jerry_stand_rect

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game = False
            if event.key == pygame.K_d:
                jerry_move = 15
            if event.key == pygame.K_a:
                jerry_move = -15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                jerry_move = 0
            if event.key == pygame.K_a:
                jerry_move = 0

    jerry_stand_rect.x += jerry_move

    surface.blit(kitchen, (0, 0))

    if plate_rect.y < 660:
        blit_plate(plate, plate_rect.x, plate_rect.y)
        plate_rect.y += 18
    else:
        if plate_rect.colliderect(jerry_stand_rect):
            plate_rect.x = randint(0, surface.get_width() - plate.get_width())
            plate_rect.y = 0 - plate.get_height()
            current_score += 1
        else:
            blit_plate(broken_plate, plate_rect.x, plate_rect.y)
            pause += 1
            if pause == 10:
                plate_rect.x = randint(0, surface.get_width() - plate.get_width())
                plate_rect.y = 0 - plate.get_height()
                pause = 0
                broken_plates += 1

    score(current_score, broken_plates)

    # blit stationary image of jerry if movement key is not being pressed
    if jerry_move == 0:
        blit_jerry(jerry_stand, jerry_stand_rect.x, jerry_stand_rect.y)

    # move jerry to the right
    elif jerry_move > 0:
        blit_jerry(jerry_run_right, jerry_stand_rect.x, jerry_stand_rect.y + 18)

    # move jerry to the left
    else:
        blit_jerry(jerry_run_left, jerry_stand_rect.x, jerry_stand_rect.y + 18)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()