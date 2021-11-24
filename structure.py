import sys

import pygame, gameplay

mid_area = pygame.Rect(220, 180, 130, 120)
mid_right = pygame.Rect(350, 180, 130, 120)
mid_left = pygame.Rect(90, 180, 130, 120)

top_area = pygame.Rect(220, 60, 130, 120)
top_right = pygame.Rect(350, 60, 130, 120)
top_left = pygame.Rect(90, 60, 130, 120)

btm_area = pygame.Rect(220, 300, 130, 120)
btm_right = pygame.Rect(350, 300, 130, 120)
btm_left = pygame.Rect(90, 300, 130, 120)

red = (255, 0, 0)
blue = (0, 0, 255)
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
# move by 155
radius = 50
draw_o = [
    [285, 120]
]
FPS = 60
rect_area_setting = pygame.Rect(210, 250, 170, 40)
rect_area_game = pygame.Rect(210, 200, 170, 40)


def display_window(screen):
    value = True
    clock = pygame.time.Clock()
    main_menu(screen)
    while value:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                value = False
            if event.type == pygame.MOUSEBUTTONUP:
                if rect_area_game.collidepoint(event.pos):
                    draw_game_outlier(screen, red, points)
                    gameplay.start_game(screen, FPS, mid_area, mid_left, mid_right, top_area, top_right, top_left,
                                        btm_area, btm_right, btm_left)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    value = False
        # main_menu(screen)
        # print(f"fps: {clock.get_fps()}")
        pygame.display.update()


def main_menu(screen):
    screen.fill((0, 0, 0))
    # pygame.font.init()
    game_font = pygame.font.SysFont("Comic Sans MS", 30)
    text_surface = game_font.render("Main Menu", False, red)
    screen.blit(text_surface, (220, 120))  # draws image on to another, in this case text on the screen
    menu_box(screen, "Comic Sans MS", "Player One", 210, 200, 170, 40, 222, 195)
    menu_box(screen, "Comic Sans MS", "Settings", 210, 250, 170, 40, 240, 245)
    pygame.display.update()


def menu_box(screen, font, text, x, y, width, height, a, b):
    pygame.draw.rect(screen, red, (x, y, width, height), width=3)
    game_font = pygame.font.SysFont(font, 30)
    text_surface = game_font.render(text, False, red)
    screen.blit(text_surface, (a, b))


def draw_game_outlier(screen, color, coordinates):
    screen.fill((0, 0, 0))
    # print("screen")
    pygame.draw.line(screen, color, coordinates[0], coordinates[1], width=3)
    pygame.draw.line(screen, color, coordinates[2], coordinates[3], width=3)
    pygame.draw.line(screen, color, coordinates[4], coordinates[5], width=3)
    pygame.draw.line(screen, color, coordinates[6], coordinates[7], width=3)
    pygame.display.update()


def draw_cross(screen, x, y):
    pygame.draw.line(screen, red, (draw_x[0][0] + x, draw_x[0][1] + y),
                     (draw_x[1][0] + x, draw_x[1][1] + y), width=3)
    pygame.draw.line(screen, red, (draw_x[2][0] + x, draw_x[2][1] + y),
                     (draw_x[3][0] + x, draw_x[3][1] + y), width=3)


def draw_circle(screen, x, y):
    pygame.draw.circle(screen, blue, (draw_o[0][0] + x, draw_o[0][1] + y), radius, width=3)


def score_board(screen):
    pygame.draw.rect(screen, (10, 10, 100, 40), width=3)
