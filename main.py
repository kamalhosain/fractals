import pygame
import button

pygame.init()

#window setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BG_COLOR = (51, 51, 102)

#create window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Fractals")

#load images
img_title_big = pygame.image.load("images/title_big.png").convert_alpha()
img_title_small = pygame.image.load("images/title_small.png").convert_alpha()
img_choose_one = pygame.image.load("images/choose_one.png").convert_alpha()
img_start_button = pygame.image.load("images/start_button.png").convert_alpha()
img_exit_button = pygame.image.load("images/exit_button.png").convert_alpha()
img_mandelbrot_button = pygame.image.load("images/mandelbrot_button.png").convert_alpha()
img_sierpinski_button = pygame.image.load("images/sierpinski_button.png").convert_alpha()
img_koch_button = pygame.image.load("images/koch_button.png").convert_alpha()
img_julia_button = pygame.image.load("images/julia_button.png").convert_alpha()
img_newton_button = pygame.image.load("images/newton_button.png").convert_alpha()
img_barnsley_button = pygame.image.load("images/barnsley_button.png").convert_alpha()

#create button instances
exit_button = button.Button(100, 200, img_exit_button)

#game loop
flag = True
while flag:

    SCREEN.fill(BG_COLOR)

    if exit_button.draw(SCREEN):
        flag = False

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    pygame.display.update()

pygame.quit()

