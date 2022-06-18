from geometry import *
import pygame
from menu import Menu, Actions


# variables
pygame.display.set_caption('2D Geometry Visualizer')
pygame.display.set_icon(pygame.image.load('resources/pictures/icon.png'))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
points = list()
mainMenu = Menu()

print('I wonder if they\'re looking at the console')

# main loop
outer_layer = list()
convex_layers = []
previous_mouse_state = False
while True:
    screen.fill(WHITE)
    mainMenu.render(screen)
    # ticks (and leeches)
    mainMenu.tick()
    if Actions.CLEAR_SCREEN:
        points = []
        outer_layer = []
        convex_layers = []
        Actions.CLEAR_SCREEN = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if pygame.mouse.get_pressed()[0] and not previous_mouse_state and Actions.ADD_POINTS:
            # print('calculating layers')
            add_point(points, *pygame.mouse.get_pos())
        if Actions.DRAW_CONVEX_LAYERS:
            convex_layers = calculate_convex_layers(points)
        elif Actions.DRAW_CONVEX_HULL:
            outer_layer = calculate_convex_layer(points)
            # print('done')
        previous_mouse_state = pygame.mouse.get_pressed()[0]

    for point in points:
        pygame.draw.circle(screen, BLACK, (point.x, point.y), 5)
    if Actions.DRAW_CONVEX_LAYERS:
        color = 0
        for layer in convex_layers:
            if color != len(COLORS):
                draw_polygon(screen, layer, COLORS[color])
                color += 1
            else:
                color = 0
                draw_polygon(screen, layer, COLORS[color])
                color += 1
    elif Actions.DRAW_CONVEX_HULL:
        draw_polygon(screen, outer_layer, BLACK)

    # draw_polygon(screen, calculate_convex_layer(points))

    pygame.display.update()
