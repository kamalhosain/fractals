import pygame

# Define color palette
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Draw Sierpinski's triangle
def draw_sierpinski(screen, x, y, size, level):

    if level == 0:
        pygame.draw.polygon(screen, WHITE, [(x, y), (x + size, y), (x + size / 2, y + size)], 0)
    else:
        draw_sierpinski(screen, x, y, size / 2, level - 1)
        draw_sierpinski(screen, x + size / 2, y, size / 2, level - 1)
        draw_sierpinski(screen, x + size / 4, y + size / 2, size / 2, level - 1)


def main_sierpinski(screen):

    screen.fill(BLACK)

    draw_sierpinski(screen, 0, 0, 600, 5)

    flag = True
    while flag:

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                flag = False

        pygame.display.update()