import pygame

pygame.init()

#window setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BG_COLOR = (120, 126, 161)

#create window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Fractals")

#define fonts and colors
TITLE_FONT = "impact"
TITLE_SIZE = 90
TEXT_COLOR = (255, 255, 255)
TEXT_BOLD = False

#define title
title_font = pygame.font.SysFont(TITLE_FONT, TITLE_SIZE, TEXT_BOLD)
title = title_font.render("FRACTALS", True, TEXT_COLOR)

#define title position
title_x_position = (SCREEN_WIDTH - title.get_width()) / 2  #centered on the x axis
title_y_position = SCREEN_HEIGHT / 4

#game loop
flag = True
while flag:

    SCREEN.fill(BG_COLOR)
    SCREEN.blit(title,(title_x_position,title_y_position))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    pygame.display.update()

pygame.quit()

