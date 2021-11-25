import sys
import pygame, gameplay


red = (255, 0, 0)
blue = (0, 0, 255)
points = [
    (220, 60), (220, 420),
    (350, 60), (350, 420),
    (90, 180), (480, 180),
    (90, 300), (480, 300)
]
radius = 50
draw_o = [
    [285, 120]
]


def main_menu(screen):
    # screen.fill((0, 0, 0))
    # pygame.font.init()
    game_font = pygame.font.SysFont("Comic Sans MS", 30)
    text_surface = game_font.render("Main Menu", False, red)
    screen.blit(text_surface, (220, 120))  # draws image on to another, in this case text on the screen
    menu_box(screen, "Comic Sans MS", "Player One", 210, 200, 170, 40, 222, 195)
    menu_box(screen, "Comic Sans MS", "Settings", 210, 250, 170, 40, 240, 245)
    # pygame.display.update()


def menu_box(screen, font, text, x, y, width, height, a, b):
    pygame.draw.rect(screen, red, (x, y, width, height), width=3)
    game_font = pygame.font.SysFont(font, 30)
    text_surface = game_font.render(text, False, red)
    screen.blit(text_surface, (a, b))


def draw_game_outlier(screen, color, line_bg, coordinates):
    screen.fill(color)
    pygame.draw.line(screen, line_bg, coordinates[0], coordinates[1], width=15)
    pygame.draw.line(screen, line_bg, coordinates[2], coordinates[3], width=15)
    pygame.draw.line(screen, line_bg, coordinates[4], coordinates[5], width=15)
    pygame.draw.line(screen, line_bg, coordinates[6], coordinates[7], width=15)
    # pygame.display.update()


def draw_cross(screen, draw_x, x, y):
    pygame.draw.line(screen, red, (draw_x[0][0] + x, draw_x[0][1] + y),
                     (draw_x[1][0] + x, draw_x[1][1] + y), width=3)
    pygame.draw.line(screen, red, (draw_x[2][0] + x, draw_x[2][1] + y),
                     (draw_x[3][0] + x, draw_x[3][1] + y), width=3)


def draw_circle(screen, x, y):
    pygame.draw.circle(screen, blue, (draw_o[0][0] + x, draw_o[0][1] + y), radius, width=3)


def score_board(screen):
    pygame.draw.rect(screen, (10, 10, 100, 40), width=3)
