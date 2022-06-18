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
        self.mouse_released = False
        self.add_points_btn = None
        self.convex_hull_btn = None
        self.convex_layers_btn = None
        self.clear_screen_btn = None
        self.add_points_btn_color = Menu.NORMAL_BUTTON_COLOR
        self.convex_hull_btn_color = Menu.NORMAL_BUTTON_COLOR
        self.convex_layers_btn_color = Menu.NORMAL_BUTTON_COLOR
        self.clear_screen_btn_color = Menu.NORMAL_BUTTON_COLOR

    def _render_add_points(self, screen):
        text_obj = default_font.render('Add Points', True, BLACK)
        self.add_points_btn = button = pygame.Rect(32, 32, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(screen, self.add_points_btn_color, button)
        for i in range(4):
            pygame.draw.rect(screen, (128, 128, 128), (32 - i, 32 - i, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(text_obj, (32 + BUTTON_WIDTH / 4 - len('Add Points'), 36 + BUTTON_HEIGHT / 4))

    def _render_convex_hull(self, screen):
        text_obj = default_font.render('Convex Hull', True, BLACK)
        self.convex_hull_btn = button = pygame.Rect(32, 100, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(screen, self.convex_hull_btn_color, button)
        for i in range(4):
            pygame.draw.rect(screen, (128, 128, 128), (32 - i, 100 - i, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(text_obj, (32 + BUTTON_WIDTH / 4 - len('Add Points'), 104 + BUTTON_HEIGHT / 4))

    def _render_convex_layers(self, screen):
        text_obj = default_font.render('Convex Hull Layers', True, BLACK)
        self.convex_layers_btn = button = pygame.Rect(200, 32, BUTTON_WIDTH * 1.5, BUTTON_HEIGHT)
        pygame.draw.rect(screen, self.convex_layers_btn_color, button)
        for i in range(4):
            pygame.draw.rect(screen, (128, 128, 128), (200 - i, 32 - i, BUTTON_WIDTH * 1.5, BUTTON_HEIGHT), 1)
        screen.blit(text_obj, (200 + BUTTON_WIDTH / 4 - len('Add Points'), 36 + BUTTON_HEIGHT / 4))

    def _render_clear_screen(self, screen):
        text_obj = default_font.render('Clear', True, BLACK)
        self.clear_screen_btn = button = pygame.Rect(200, 100, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(screen, self.clear_screen_btn_color, button)
        for i in range(4):
            pygame.draw.rect(screen, (128, 128, 128), (200 - i, 100 - i, BUTTON_WIDTH, BUTTON_HEIGHT), 1)
        screen.blit(text_obj, (200 + BUTTON_WIDTH / 4 - len('Add Points'), 104 + BUTTON_HEIGHT / 4))

    def _check_mouse(self):
        if pygame.mouse.get_pressed()[0]:
            self.mouse_clicked = not self.mouse_down
            self.mouse_down = True
        else:
            self.mouse_clicked = False
            self.mouse_down = False

    def _check_mouse_released(self):
        if not pygame.mouse.get_pressed()[0]:
            self.mouse_released = self.mouse_down
        else:
            self.mouse_released = False

    def _check_add_points_clicked(self):
        if pygame.Rect(self.add_points_btn).collidepoint(pygame.mouse.get_pos()):
            Actions.ADD_POINTS = not Actions.ADD_POINTS
            if Actions.ADD_POINTS:
                self.add_points_btn_color = Menu.PRESSED_BUTTON_COLOR
            else:
                self.add_points_btn_color = Menu.NORMAL_BUTTON_COLOR

    def _check_convex_hull_clicked(self):
        if pygame.Rect(self.convex_hull_btn).collidepoint(pygame.mouse.get_pos()):
            Actions.DRAW_CONVEX_HULL = not Actions.DRAW_CONVEX_HULL
            if Actions.DRAW_CONVEX_HULL:
                self.convex_hull_btn_color = Menu.PRESSED_BUTTON_COLOR
            else:
                self.convex_hull_btn_color = Menu.NORMAL_BUTTON_COLOR

    def _check_convex_layers_clicked(self):
        if pygame.Rect(self.convex_layers_btn).collidepoint(pygame.mouse.get_pos()):
            Actions.DRAW_CONVEX_LAYERS = not Actions.DRAW_CONVEX_LAYERS
            if Actions.DRAW_CONVEX_LAYERS:
                self.convex_layers_btn_color = Menu.PRESSED_BUTTON_COLOR
            else:
                self.convex_layers_btn_color = Menu.NORMAL_BUTTON_COLOR

    def _check_clear_pressed(self):
        if self.mouse_released:
            self.clear_screen_btn_color = Menu.NORMAL_BUTTON_COLOR
        if pygame.Rect(self.clear_screen_btn).collidepoint(pygame.mouse.get_pos()):
            Actions.CLEAR_SCREEN = self.mouse_released
            if self.mouse_clicked: self.clear_screen_btn_color = Menu.PRESSED_BUTTON_COLOR

    def tick(self):
        self._check_mouse_released()
        self._check_mouse()
        if self.mouse_clicked:
            self._check_add_points_clicked()
            self._check_convex_hull_clicked()
            self._check_convex_layers_clicked()
            self._check_clear_pressed()
        if self.mouse_released:
            self._check_clear_pressed()

    def render(self, screen):
        pygame.draw.rect(screen, 'grey', self.background)
        self._render_add_points(screen)
        self._render_convex_hull(screen)
        self._render_convex_layers(screen)
        self._render_clear_screen(screen)
