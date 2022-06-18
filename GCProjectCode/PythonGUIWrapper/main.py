from geometry import *
import pygame
from menu import Menu, Actions


# variables
pygame.display.set_caption('2D Geometry Visualizer')
pygame.display.set_icon(pygame.image.load('resources/pictures/icon.png'))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
points = []
outer_layer = []
convex_layers = []
mainMenu = Menu()

print('I wonder if they\'re looking at the console')

# main loop
# we need this because pygame doesn't offer a way of knowing if the mouse was just clicked
# all we get is the press state for each button which will be true as long as a mouse is held
previous_mouse_state = False
while True:
    # the screen is reset every frame so that we can redraw
    screen.fill(WHITE)
    # render the main menu
    mainMenu.render(screen)
    # ticks (and leeches)
    mainMenu.tick()
    # this only clears the points from the screen and the lines, not the menu too
    # by emptying the arrays nothing will be drawn anymore until added again
    if Actions.CLEAR_SCREEN:
        points = []
        outer_layer = []
        convex_layers = []
        # this action must be reset once executed
        Actions.CLEAR_SCREEN = False

    # this for handles mouse events and such, figure it out yourself
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if pygame.mouse.get_pressed()[0] and not previous_mouse_state:
            # print('calculating layers')
            if Actions.ADD_POINTS:
                add_point(points, *pygame.mouse.get_pos())
            elif Actions.REMOVE_POINTS:
                remove_point(points, pygame.mouse.get_pos())
        if Actions.DRAW_CONVEX_LAYERS:
            convex_layers = calculate_convex_layers(points)
        elif Actions.DRAW_CONVEX_HULL:
            outer_layer = calculate_convex_layer(points)
        previous_mouse_state = pygame.mouse.get_pressed()[0]

    # this is the section for drawing the points and eventual polygons on the screen
    # the convex layers get drawn if the toggle is turned on by clicking the button
    if Actions.DRAW_CONVEX_LAYERS:
        # the layers get drawn with alternating colors
        color = 0
        for layer in convex_layers:
            if color != len(COLORS):
                draw_polygon(screen, layer, COLORS[color])
                color += 1
            else:
                color = 0
                draw_polygon(screen, layer, COLORS[color])
                color += 1
    # the convex hull gets drawn if its toggle is on and the toggle for convex layers is off
    elif Actions.DRAW_CONVEX_HULL:
        draw_polygon(screen, outer_layer, BLACK, 3)
    # the points always gets drawn
    for point in points:
        pygame.draw.circle(screen, BLACK, (point.x, point.y), 5)

    # updates the screen every frame
    pygame.display.update()
