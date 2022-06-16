from geometry import Point2D
from geometry import WIDTH, BLACK, LIGHT_BLUE, BLUE
import pygame

BUTTON_WIDTH, BUTTON_HEIGHT = 128, 48

pygame.init()


class Actions:
    ADD_POINTS = False
    DRAW_CONVEX_HULL = False
    DRAW_CONVEX_LAYERS = False
    CLEAR_SCREEN = False


default_font = pygame.font.SysFont(None, 24)


class Menu:
    NORMAL_BUTTON_COLOR = LIGHT_BLUE
    PRESSED_BUTTON_COLOR = BLUE

    def __init__(self):
        self.origin = Point2D(0, 0)
        self.size = Point2D(WIDTH, 200)
        self.background = pygame.Rect(0, 0, WIDTH, 200)
        self.mouse_clicked = False
        self.mouse_down = False
        self.add_points_btn = None
        self.add_points_btn_color = Menu.NORMAL_BUTTON_COLOR

    def _render_add_points(self, screen):
        text_obj = default_font.render('Add Points', True, BLACK)
        # screen.blit(text_obj, text_rect)
        # self.add_points_checkbox = None
        self.add_points_btn = button = pygame.Rect(32, 32, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(screen, self.add_points_btn_color, button)
        for i in range(4):
            pygame.draw.rect(screen, (128, 128, 128), (32 - i, 32 - i, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(text_obj, (32 + BUTTON_WIDTH / 4 - len('Add Points'), 36 + BUTTON_HEIGHT / 4))

    def _check_mouse(self):
        if pygame.mouse.get_pressed()[0]:
            if not self.mouse_down:
                self.mouse_clicked = True
            else:
                self.mouse_clicked = False
            # print('mouse down')
            self.mouse_down = True
        else:
            self.mouse_clicked = False
            self.mouse_down = False

    def _check_add_points_clicked(self):
        if pygame.Rect(self.add_points_btn).collidepoint(pygame.mouse.get_pos()):
            Actions.ADD_POINTS = not Actions.ADD_POINTS
            if Actions.ADD_POINTS:
                self.add_points_btn_color = Menu.PRESSED_BUTTON_COLOR
            else:
                self.add_points_btn_color = Menu.NORMAL_BUTTON_COLOR

    def tick(self):
        self._check_mouse()
        if self.mouse_clicked:
            self._check_add_points_clicked()

    def render(self, screen):
        pygame.draw.rect(screen, 'grey', self.background)
        self._render_add_points(screen)
