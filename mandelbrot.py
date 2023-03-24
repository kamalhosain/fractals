import pygame

# Define color palette
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Determinate if a point is in the Mandelbrot set
def in_mandelbrot(x, y, max_iterations):
    a = 0
    b = 0

    for i in range(max_iterations):
        a_temp = a * a - b * b + x
        b = 2 * a * b + y
        a = a_temp

        if abs(a + b) > 16:
            return i

    return max_iterations

# Draw the Mandelbrot fractal
def draw_mandelbrot(screen, screen_width, screen_height, max_iterations):

    screen.fill(BLACK)

    flag = True
    while flag:

        for x_pixel in range(screen_width):
            for y_pixel in range(screen_height):
                x = (x_pixel - screen_width / 2) * 4 / screen_width
                y = (y_pixel - screen_height / 2) * 4 / screen_width
                color = (min(in_mandelbrot(x, y, max_iterations) * 16, 255), 0, 0)
                #color_value = min(in_mandelbrot(x, y, max_iterations), 255)
                #color = (color_value, 0, 0)
                pygame.draw.rect(screen, color, (x_pixel, y_pixel, 1, 1), 0)

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                flag = False

        pygame.display.flip()
