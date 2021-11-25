import sys
import pygame, gameplay


red = (255, 0, 0)
blue = (0, 0, 255)
SQUARE = 200
radius = 50


def main_menu(screen):
    game_font = pygame.font.SysFont("Comic Sans MS", 30)
    text_surface = game_font.render("Main Menu", False, red)
    screen.blit(text_surface, (220, 120))  # draws image on to another, in this case text on the screen
    menu_box(screen, "Comic Sans MS", "Player One", 210, 200, 170, 40, 222, 195)
    menu_box(screen, "Comic Sans MS", "Settings", 210, 250, 170, 40, 240, 245)


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


def score_board(screen):
    pygame.draw.rect(screen, (10, 10, 100, 40), width=3)


def draw_x(screen, row, col):
    pygame.draw.line(screen, (0, 0, 0), (row * SQUARE + SQUARE / 4, (col * SQUARE) + SQUARE / 4),
                     ((SQUARE * row - SQUARE / 4) + SQUARE, (col * SQUARE - SQUARE / 4) + SQUARE), width=15)
    pygame.draw.line(screen, (0, 0, 0), (row * SQUARE + SQUARE / 4, (col * SQUARE - SQUARE / 4) + SQUARE),
                     ((SQUARE * row - SQUARE / 4) + SQUARE, (col * SQUARE) + 50), width=15)


def draw_o(screen, row, col):
    pygame.draw.circle(screen, (0, 0, 0), (row * SQUARE + SQUARE / 2, (col * SQUARE) + SQUARE / 2), radius=50, width=15)


def draw_horizontal_line(screen, row, col):
    pygame.draw.line(screen, (0,0,0), (row * SQUARE + SQUARE / 4, (col * SQUARE) + SQUARE / 2),
                     ((SQUARE * 3 - SQUARE / 4), (col * SQUARE) + SQUARE / 2), width=15)
    # print("HERE")


def draw_vertical_line(screen, row, col):
    pygame.draw.line(screen, (0,0,0), (row * SQUARE + SQUARE / 4, (col * SQUARE) + SQUARE / 2),
                     (row * SQUARE + SQUARE / 4, (3 * SQUARE) - SQUARE / 2), width=15)


def draw_asc_diagonal(screen, row, col):
    pygame.draw.line(screen, (255, 0, 0), (row * SQUARE + SQUARE / 2, SQUARE / 2),
                     (abs(col * SQUARE - SQUARE / 2), (3 * SQUARE) - SQUARE / 2), width=15)


def draw_dsc_diagonal(screen, row, col):
    pygame.draw.line(screen, (255, 0, 0), (row * SQUARE + SQUARE / 2, (3 * SQUARE) - SQUARE / 2),
                     (abs(row * SQUARE - SQUARE / 2), (3 * SQUARE) + SQUARE / 2), width=15)
