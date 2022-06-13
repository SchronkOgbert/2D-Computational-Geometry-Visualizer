import pygame
import numpy as np
import math

# constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 1280, 720


# classes
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.__str__())

    def to_arg(self):
        return f'{self.x} {self.y}'


# variables
pygame.display.set_caption('2D Geometry Visualizer')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
points = set()


# functions
def add_point(x, y):
    global points
    init_size = len(points)
    buffer = Point2D(x, y)
    points.add(buffer)
    if len(points) == init_size:
        print(f'point {buffer} already exists')
        return
    print(f'added point {buffer}')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if pygame.mouse.get_pressed()[0]:
            add_point(*pygame.mouse.get_pos())
            print(points)

    screen.fill(WHITE)
    for point in points:
        pygame.draw.circle(screen, BLACK, (point.x, point.y), 5)

    pygame.display.update()
