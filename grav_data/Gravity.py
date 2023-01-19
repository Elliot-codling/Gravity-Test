#gravity test
from engine import game_engine_130123 as engine
import pygame, os
file_dir = os.getcwd()

#create window
w, h = 400, 400
window = engine.window.define("Gravity Test", w, h)

#variables
run = True
clock = pygame.time.Clock()
gotSquare = False
playerSpeed = 4

#lists
display_sprite = []
square = engine.properties_object("square", f"{file_dir}/textures/green.png", 100, 100, 32, 32, False)
display_sprite += [square]

def moveSquare():
    global playerSpeed
    square.x = pygame.mouse.get_pos()[0] - 16
    square.y = pygame.mouse.get_pos()[1] - 16
    playerSpeed = 4

def main():
    global gotSquare, playerSpeed                #check if the player has a hold of the square
    if not pygame.mouse.get_pressed()[0]:
        gotSquare = False
    elif engine.mouse.collision("square", display_sprite):
        gotSquare = True

    if gotSquare:
        moveSquare()
    else:
        engine.player.down(square, playerSpeed, h - 32)
        playerSpeed += 2

        #check if under the ground
        if square.y + square.height > h:
            square.y = h - square.height

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    main()
    engine.window.update(window, None, display_sprite)
    clock.tick(60)
pygame.quit()