import sys

import pygame, structure, gameplay

border = (11, 101, 119)
blue = (0, 0, 255)
RECT_P1 = (210, 200, 170, 40)
RECT_P2 = (210, 250, 170, 40)


def setting(screen, FPS, BG, COORDINATES):
    value = True
    setting_screen(screen)
    while value:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    structure.main_menu(screen)
                    value = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(RECT_P1).collidepoint(event.pos):
                    gameplay.start_game(screen, FPS, BG, COORDINATES, mode=1)
                if pygame.Rect(RECT_P2).collidepoint(event.pos):
                    gameplay.start_game(screen, FPS, BG, COORDINATES, mode=2)
        pygame.display.update()


def setting_screen(screen):
    screen.fill((70, 206, 188))
    game_font = pygame.font.SysFont("Comic Sans MS", 40)
    text_surface = game_font.render("Settings", False, border)
    screen.blit(text_surface, (220, 120))  # draws image on to another, in this case text on the screen
    setting_box(screen, "Comic Sans MS", "One Player", 210, 200, 170, 40, 222, 195)
    setting_box(screen, "Comic Sans MS", "Two Player", 210, 250, 170, 40, 222, 245)


def setting_box(screen, font, text, x, y, width, height, a, b):
    pygame.draw.rect(screen, border, (x, y, width, height), width=5)
    game_font = pygame.font.SysFont(font, 30)
    text_surface = game_font.render(text, False, border)
    screen.blit(text_surface, (a, b))
