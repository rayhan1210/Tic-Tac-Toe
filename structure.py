import pygame

points = [
    (220, 60), (220, 420),
    (350, 60), (350, 420),
    (90, 180), (480, 180),
    (90, 300), (480, 300)
]
draw_x = [
    [230, 80], [340, 160],
    [340, 80], [230, 160]
]
red = 255, 0, 0

class GameStructure:
    # def __init__(self):
    #     self.size = self.max_width, self.max_height = 600, 500

    def display_window(self, screen):
        self.draw_game_outlier(screen, red, points)

    @staticmethod
    def draw_game_outlier(screen, color, coordinates):
        pygame.draw.line(screen, color, coordinates[0], coordinates[1], width=3)
        pygame.draw.line(screen, color, coordinates[2], coordinates[3], width=3)
        pygame.draw.line(screen, color, coordinates[4], coordinates[5], width=3)
        pygame.draw.line(screen, color, coordinates[6], coordinates[7], width=3)

    def draw_gamechar_x(self, screen, x, y):
        pygame.draw.line(screen, (255, 0, 0), (draw_x[0][0] + x, draw_x[0][1] + y),
                         (draw_x[1][0] + x, draw_x[1][1] + y), width=3)
        pygame.draw.line(screen, (255, 0, 0), (draw_x[2][0] + x, draw_x[2][1] + y),
                         (draw_x[3][0] + x, draw_x[3][1] + y), width=3)

