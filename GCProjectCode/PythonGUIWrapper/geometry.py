import subprocess
import pygame

# constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 170, 0)
YELLOW = (170, 170, 0)
RED = (170, 0, 0)
BLUE = (0, 128, 255)
LIGHT_BLUE = (51,187,255)
WIDTH, HEIGHT = 1600, 900

COLORS = [GREEN, YELLOW, RED, BLUE]


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
        if abs(self.x - other.x) < 10 and abs(self.y - other.y) < 10: return True
        return False

    def __hash__(self):
        return hash(self.__str__())

    def to_arg(self):
        return f'{self.x} {self.y}'


# functions
def add_point(points, x, y):
    buffer = Point2D(x, y)
    if y < 200: return
    if buffer in points:
        # print(f'point {buffer} already exists')
        return
    points.append(buffer)
    # print(f'added point {buffer}')


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
            values = point_row.split(' ')
            res.append(Point2D(int(values[0]), int(values[1])))
    except Exception as e:
        pass
        # print(e)
    return res


def calculate_convex_layers(points):
    sublayer = points
    layers = []
    while len(sublayer):
        layers.append(calculate_convex_layer(sublayer))
        last_layer = sublayer
        sublayer = set()
        for point in last_layer:
            if point not in layers[-1]:
                sublayer.add(point)
    return layers


def draw_polygon(screen, pts, color = BLACK):
    if not len(pts): return
    for i in range(len(pts) - 1):
        pygame.draw.line(screen, color, (pts[i].x, pts[i].y), (pts[i + 1].x, pts[i + 1].y), 4)
    if pts[0] != pts[-1]:
        pygame.draw.line(screen, color, (pts[0].x, pts[0].y), (pts[-1].x, pts[-1].y), 4)