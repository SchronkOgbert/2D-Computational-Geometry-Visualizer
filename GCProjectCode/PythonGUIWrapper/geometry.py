import subprocess
import pygame

# constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 170, 0)
YELLOW = (170, 170, 0)
RED = (170, 0, 0)
BLUE = (0, 128, 255)
LIGHT_BLUE = (51, 187, 255)
WIDTH, HEIGHT = 1600, 900

COLORS = [GREEN, YELLOW, RED, BLUE] # these are the colors used to alternate between the convex layers


# classes
class Point2D:
    def __init__(self, x, y):
        """
        this one is pretty obvious
        :param x: x coord
        :param y: y coord
        """
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x} {self.y})'

    def __eq__(self, other):
        if abs(self.x - other.x) < 10 and abs(self.y - other.y) < 10: return True
        return False

    def __hash__(self):
        return hash(self.__str__())

    def to_arg(self):
        return f'{self.x} {self.y}'

    def collide(self, coords: tuple):
        """
        the collision is not exact, as it's very unlikely you will hit the exact pixels of the point
        :param coords: coords to check collision for
        :return: whether that point is within the collision square
        """
        return self.x + 10 >= coords[0] >= self.x - 10 and self.y + 10 >= coords[1] >= self.y - 10


# functions
def add_point(points, x, y):
    """
    adds a point to the given coord, which is always the mouse location in this program
    :param points: the list to which we add the point
    :param x: x coord
    :param y: y coord
    :return: aborts if a point cannot be added
    """
    buffer = Point2D(x, y)
    if y < 200: return
    if buffer in points:
        return
    points.append(buffer)


def remove_point(points: list, position: tuple):
    """
    removes a point from the given list and position if one such point can be found
    :param points: list from which to remove
    :param position: position to check
    """
    for point in points:
        if Point2D(point.x, point.y).collide(position):
            points.remove(point)


def make_command_line_args(pts):
    """
    parses the coordinates of all the points into a string that will be passed to the c++ program through the cl
    :param pts: list of points
    :return: string with coordinates
    """
    res = ""
    for point in pts:
        res += f' {point.to_arg()}'
    return res


def calculate_convex_layer(pts):
    """
    the outer most convex layer is calculated in a c++ program that uses cgal
    the c++ program is also available in this repo
    :param pts: the list of points to be calculated
    :return: the list of points that make the convex hull
    """
    res = []
    try:
        points_str = subprocess.check_output(f"binaries/AlgorithmsCalculator.exe{make_command_line_args(pts)}").decode()
        # a little parsing is needed since the program outputs a string
        # again the program is available in this repo
        points_rows = points_str.split('\n')
        points_rows.remove('')
        for point_row in points_rows:
            values = point_row.split(' ')
            res.append(Point2D(int(values[0]), int(values[1])))
    except Exception as e:
        pass
        # print(e)
    return res


def calculate_convex_layers(points):
    """
    calculates all the convex layers of the given points, by gradually stripping the array of the points that have
    been calculated already and calling the c++ program multiple times
    :param points: the list of points to be calculated
    :return: a list with lists of points for each layer
    """
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


def draw_polygon(screen, pts, color=BLACK, fill=0):
    """
    this function also draws lines if there are only 2 points
    :param screen: screen to draw on
    :param pts: points to be drawn
    :param color: color to draw with
    :param fill: 0-fill shape, < 0 do not draw, > 0 set line thiccness
    """
    if len(pts) > 2:
        pygame.draw.polygon(screen, color,
                            [tuple(map(int, point.__repr__().replace('(', '').replace(')', '').split(' '))) for point in
                             pts], fill)
    elif len(pts) == 2:
        if fill == 0:
            fill = 3
        pygame.draw.line(screen, color, (pts[0].x, pts[0].y), (pts[1].x, pts[1].y), fill)

