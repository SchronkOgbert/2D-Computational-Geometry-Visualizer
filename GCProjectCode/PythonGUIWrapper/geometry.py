import subprocess
import pygame

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


# functions
def add_point(points, x, y):
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
            values = point_row.split(' ')
            res.append(Point2D(int(values[0]), int(values[1])))
    except Exception as e:
        print(e)
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


def draw_polygon(screen, pts):
    if not len(pts): return
    for i in range(len(pts) - 1):
        pygame.draw.line(screen, BLACK, (pts[i].x, pts[i].y), (pts[i + 1].x, pts[i + 1].y), 3)
    if pts[0] != pts[-1]:
        pygame.draw.line(screen, BLACK, (pts[0].x, pts[0].y), (pts[-1].x, pts[-1].y), 3)