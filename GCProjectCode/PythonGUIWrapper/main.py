from geometry import *
import pygame


# variables
pygame.display.set_caption('2D Geometry Visualizer')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
points = list()


# main loop
outer_layer = list()
convex_layers = []
previous_mouse_state = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if pygame.mouse.get_pressed()[0] and not previous_mouse_state:
            # print('calculating layers')
            add_point(points, *pygame.mouse.get_pos())
            outer_layer = calculate_convex_layer(points)
            convex_layers = calculate_convex_layers(points)
            # print('done')
        previous_mouse_state = pygame.mouse.get_pressed()[0]

    screen.fill(WHITE)
    for point in points:
        pygame.draw.circle(screen, BLACK, (point.x, point.y), 5)
    color = 0
    for layer in convex_layers:
        if color != len(COLORS):
            draw_polygon(screen, layer, COLORS[color])
            color += 1
        else:
            color = 0
            draw_polygon(screen, layer, COLORS[color])
            color += 1

    # draw_polygon(screen, calculate_convex_layer(points))

    pygame.display.update()
