import pygame

border = (11, 101, 119)
blue = (0, 0, 255)
# CROSS_COLOR = (252, 240, 4)
SQUARE = 200
radius = 50
FONT = "Comic Sans MS"
MENU = "Main Menu"
button = ["Play", "Setting"]
CROSS_COLOR = (45, 79, 86)
o_color = (9, 127, 96)


def main_menu(screen):
    screen.fill((70, 206, 188))
    game_font = pygame.font.SysFont(FONT, 40)
    text_surface = game_font.render(MENU, False, border)
    screen.blit(text_surface, (195, 120))  # draws image on to another, in this case text on the screen
    menu_box(screen, FONT, button[0], 210, 200, 170, 40, 262, 195)
    menu_box(screen, FONT, button[1], 210, 250, 170, 40, 240, 245)


def menu_box(screen, font, text, x, y, width, height, a, b):
    pygame.draw.rect(screen, border, (x, y, width, height), width=5)
    game_font = pygame.font.SysFont(font, 30)
    text_surface = game_font.render(text, False, border)
    screen.blit(text_surface, (a, b))


def draw_game_outlier(screen, color, line_bg, coordinates):
    screen.fill(color)
    pygame.draw.line(screen, line_bg, coordinates[0], coordinates[1], width=15)
    pygame.draw.line(screen, line_bg, coordinates[2], coordinates[3], width=15)
    pygame.draw.line(screen, line_bg, coordinates[4], coordinates[5], width=15)
    pygame.draw.line(screen, line_bg, coordinates[6], coordinates[7], width=15)
    # pygame.display.update()


def draw_x(screen, row, col):
    pygame.draw.line(screen, CROSS_COLOR, (row * SQUARE + SQUARE / 4, (col * SQUARE) + SQUARE / 4),
                     ((SQUARE * row - SQUARE / 4) + SQUARE, (col * SQUARE - SQUARE / 4) + SQUARE), width=15)
    pygame.draw.line(screen, CROSS_COLOR, (row * SQUARE + SQUARE / 4, (col * SQUARE - SQUARE / 4) + SQUARE),
                     ((SQUARE * row - SQUARE / 4) + SQUARE, (col * SQUARE) + 50), width=15)


def draw_o(screen, row, col):
    pygame.draw.circle(screen, o_color, (row * SQUARE + SQUARE / 2, (col * SQUARE) + SQUARE / 2), radius=50, width=15)


def draw_horizontal_line(screen, row, col):
    pygame.draw.line(screen, CROSS_COLOR, (row * SQUARE + SQUARE / 4, (col * SQUARE) + SQUARE / 2),
                     ((SQUARE * 3 - SQUARE / 4), (col * SQUARE) + SQUARE / 2), width=15)


def draw_vertical_line(screen, row, col):
    pygame.draw.line(screen, CROSS_COLOR, (row * SQUARE + SQUARE / 2, (col * SQUARE) + SQUARE / 4),
                     (row * SQUARE + SQUARE / 2, (3 * SQUARE) - SQUARE / 4), width=15)


def draw_asc_diagonal(screen, row, col, row2, col2):
    pygame.draw.line(screen, CROSS_COLOR, (row * SQUARE + SQUARE / 4, (col * SQUARE) + SQUARE / 4),
                     ((SQUARE * row2 - SQUARE / 4) + SQUARE, (col2 * SQUARE - SQUARE / 4) + SQUARE), width=15)


def draw_asc_diagonal2(screen, row, col, row2, col2):
    pygame.draw.line(screen, CROSS_COLOR, (row * SQUARE + SQUARE / 4, (col * SQUARE - SQUARE / 4) + SQUARE),
                     ((SQUARE * row2 - SQUARE / 4) + SQUARE, (col2 * SQUARE) + SQUARE / 4), width=15)

