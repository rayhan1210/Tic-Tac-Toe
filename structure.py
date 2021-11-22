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
    def __init__(self, max_width, max_height):
        self.size = self.max_width, self.max_height = max_width, max_height

    def display_window(self):
        screen = pygame.display.set_mode(self.size)
        self.draw_game_outlier(screen, red, points)

    @staticmethod
    def draw_game_outlier(screen, color, coordinates):
        pygame.draw.line(screen, color, coordinates[0], coordinates[1], width=3)
        pygame.draw.line(screen, color, coordinates[2], coordinates[3], width=3)
        pygame.draw.line(screen, color, coordinates[4], coordinates[5], width=3)
        pygame.draw.line(screen, color, coordinates[6], coordinates[7], width=3)

        # print(draw_x[0][1])
        # top area
        # pygame.draw.line(screen, red, (draw_x[0][0] + 135, draw_x[0][1]), (draw_x[1][0] + 135, draw_x[1][1]), width=3)
        # pygame.draw.line(screen, red, (draw_x[2][0] + 135, draw_x[2][1]), (draw_x[3][0] + 135, draw_x[3][1]), width=3)
        # pygame.draw.line(screen, red, (draw_x[0][0] - 135, draw_x[0][1]), (draw_x[1][0] - 135, draw_x[1][1]), width=3)
        # pygame.draw.line(screen, red, (draw_x[2][0] - 135, draw_x[2][1]), (draw_x[3][0] - 135, draw_x[3][1]), width=3)
        # pygame.draw.line(screen, red, (draw_x[0][0], draw_x[0][1]), (draw_x[1][0], draw_x[1][1]), width=3)
        # pygame.draw.line(screen, red, (draw_x[2][0], draw_x[2][1]), (draw_x[3][0], draw_x[3][1]), width=3)
        # mid area
        # pygame.draw.line(screen, red, (draw_x[0][0], draw_x[0][1] + 120), (draw_x[1][0], draw_x[1][1]+ 120), width=3)
        # pygame.draw.line(screen, red, (draw_x[2][0], draw_x[2][1] + 120), (draw_x[3][0], draw_x[3][1]+ 120), width=3)
        # pygame.draw.line(screen, red, (draw_x[0][0]+135, draw_x[0][1] + 120), (draw_x[1][0]+135, draw_x[1][1] + 120), width=3)
        # pygame.draw.line(screen, red, (draw_x[2][0]+135, draw_x[2][1] + 120), (draw_x[3][0]+135, draw_x[3][1] + 120), width=3)
        # pygame.draw.line(screen, red, (draw_x[0][0]-135, draw_x[0][1] + 120), (draw_x[1][0]-135, draw_x[1][1] + 120), width=3)
        # pygame.draw.line(screen, red, (draw_x[2][0]-135, draw_x[2][1] + 120), (draw_x[3][0]-135, draw_x[3][1] + 120), width=3)
        # pygame.draw.line(screen, red, (draw_x[0][0], draw_x[0][1] + 120), (draw_x[1][0], draw_x[1][1] + 120), width=3)
        # pygame.draw.line(screen, red, (draw_x[2][0], draw_x[2][1] + 120), (draw_x[3][0], draw_x[3][1] + 120), width=3)
        # bottom area
        # pygame.draw.line(screen, red, (draw_x[0][0] - 135, draw_x[0][1] + 240), (draw_x[1][0] - 135, draw_x[1][1] + 240), width=3)
        # pygame.draw.line(screen, red, (draw_x[2][0] - 135, draw_x[2][1] + 240), (draw_x[3][0] - 135, draw_x[3][1] + 240), width=3)
        # pygame.draw.line(screen, red, (draw_x[0][0] + 135, draw_x[0][1] + 240), (draw_x[1][0] + 135, draw_x[1][1] + 240), width=3)
        # pygame.draw.line(screen, red, (draw_x[2][0] + 135, draw_x[2][1] + 240), (draw_x[3][0] + 135, draw_x[3][1] + 240), width=3)
        # pygame.draw.line(screen, red, (draw_x[0][0], draw_x[0][1] + 240), (draw_x[1][0], draw_x[1][1] + 240), width=3)
        # pygame.draw.line(screen, red, (draw_x[2][0], draw_x[2][1] + 240), (draw_x[3][0], draw_x[3][1] + 240), width=3)


