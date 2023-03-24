import pygame
import button
import mandelbrot

pygame.init()

#window setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#create window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fractals")

#background color
BG_COLOR = (51, 51, 102)

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
TITLE_BIG = button.Button(65, 199, img_title_big)
TITLE_SMALL = button.Button(244, 43, img_title_small)
CHOOSE_ONE = button.Button(322.4, 130.7, img_choose_one)
START_BUTTON = button.Button(313, 420, img_start_button)
EXIT_BUTTON = button.Button(340, 523, img_exit_button)
MANDELBROT_BUTTON = button.Button(38, 180, img_mandelbrot_button)
SIERPINSKI_BUTTON = button.Button(496, 180, img_sierpinski_button)
KOCH_BUTTON = button.Button(38, 300, img_koch_button)
JULIA_BUTTON = button.Button(496, 300, img_julia_button)
NEWTON_BUTTON = button.Button(38, 420, img_newton_button)
BARNSLEY_BUTTON = button.Button(496, 420, img_barnsley_button)

#print screen1: main menu
def screen1():

    while True:

        SCREEN.fill(BG_COLOR)

        TITLE_BIG.draw(SCREEN)
        if START_BUTTON.draw(SCREEN):
            return True

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        pygame.display.update()


#print screen2: fractal selector
def screen2():

    while True:
        SCREEN.fill(BG_COLOR)

        TITLE_SMALL.draw(SCREEN)
        CHOOSE_ONE.draw(SCREEN)

        if MANDELBROT_BUTTON.draw(SCREEN):
            mandelbrot.draw_mandelbrot(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, 100)
        elif SIERPINSKI_BUTTON.draw(SCREEN):
            print("Sierpinski was clicked")
        elif KOCH_BUTTON.draw(SCREEN):
            print("Koch was clicked")
        elif JULIA_BUTTON.draw(SCREEN):
            print("Julia was clicked")
        elif NEWTON_BUTTON.draw(SCREEN):
            print("Newton was clicked")
        elif BARNSLEY_BUTTON.draw(SCREEN):
            print("Barnsley was clicked")
        elif EXIT_BUTTON.draw(SCREEN):
            return

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.update()