import os

import pygame
import subprocess

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


def make_command_line_args(pts):
    res = ""
    for point in pts:
        res += f' {point.to_arg()}'
    return res


def calculate_convex_layer(pts):
    res = list()
    try:
        points_str = subprocess.check_output(f"binaries/AlgorithmsCalculator.exe{make_command_line_args(pts)}").decode()
        points_rows = points_str.split('\n')
        # print(points_str)
        points_rows.remove('')
        for point_row in points_rows:
            print(point_row)
            values = point_row.split(' ')
            res.append(Point2D(int(values[0]), int(values[1])))
    except Exception as e:
        print(e)
    return res


def draw_convex_layer(pts):
    print(f'drawing convex layer for: \n{pts}')
    if not len(pts): return
    for i in range(len(pts) - 1):
        pygame.draw.line(screen, BLACK, (pts[i].x, pts[i].y), (pts[i + 1].x, pts[i + 1].y))
    if pts[0] != pts[-1]:
        pygame.draw.line(screen, BLACK, (pts[0].x, pts[0].y), (pts[-1].x, pts[-1].y))


outer_layer = list()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if pygame.mouse.get_pressed()[0]:
            add_point(*pygame.mouse.get_pos())
            outer_layer = calculate_convex_layer(points)

    screen.fill(WHITE)
    for point in points:
        pygame.draw.circle(screen, BLACK, (point.x, point.y), 5)
    draw_convex_layer(outer_layer)

    pygame.display.update()
