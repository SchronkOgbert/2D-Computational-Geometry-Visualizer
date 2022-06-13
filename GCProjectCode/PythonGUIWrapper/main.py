from geometry import *
import pygame


# variables
pygame.display.set_caption('2D Geometry Visualizer')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
points = set()


# main loop
outer_layer = list()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if pygame.mouse.get_pressed()[0]:
            add_point(points, *pygame.mouse.get_pos())
            outer_layer = calculate_convex_layer(points)

    screen.fill(WHITE)
    for point in points:
        pygame.draw.circle(screen, BLACK, (point.x, point.y), 5)
    for layer in calculate_convex_layers(points):
        draw_polygon(screen, layer)

    pygame.display.update()
