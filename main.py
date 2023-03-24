import pygame
import screens

#game loop
game_started = screens.screen1()

if game_started:
    screens.screen2()

pygame.quit()