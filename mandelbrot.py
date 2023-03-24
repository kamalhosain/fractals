import pygame

# Define color palette
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Define the limits of the complex plane
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

# Determines if a point belongs to the Mandelbrot set
def in_mandelbrot(complex_coord, max_iterations):
    z = 0
    for i in range(max_iterations):
        z = z*z + complex_coord
        if abs(z) > 2:
            return i
    return max_iterations


# Draw the Mandelbrot fractal
def draw_mandelbrot(screen, screen_width, screen_height, max_iterations):

    x = 0
    y = 0
    flag = True
    while flag:

        screen.fill(BLACK)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                flag = False

        #iterate over each pixel on the screen
        for x in range(screen_width):
            for y in range(screen_height):
                #convert the pixel to a coordinate in the complex plane
                complex_coord = complex(RE_START + (x / screen_width) * (RE_END - RE_START),
                            IM_START + (y / screen_height) * (IM_END - IM_START))

                #determine if the point belongs to the Mandelbrot set
                total_iterations = in_mandelbrot(complex_coord, max_iterations)

                #calculate pixel color
                color = (total_iterations % 8 * 32, total_iterations % 16 * 16, total_iterations % 32 * 8)

                #draw the pixel
                screen.set_at((x, y), color)


                pygame.display.update((x, y, 1, 1))

                #move to the next pixel
                x += 1
                if x >= screen_width:
                    x = 0
                    y += 1

                if y >= screen_height:
                    flag = False
