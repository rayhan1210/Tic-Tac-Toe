import sys

import pygame, structure, gameplay

red = (255, 0, 0)
blue = (0, 0, 255)


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
                if pygame.Rect(210, 250, 170, 40).collidepoint(event.pos):
                    gameplay.start_game(screen, FPS, BG, COORDINATES, mode=1)
                if pygame.Rect(210, 300, 170, 40).collidepoint(event.pos):
                    gameplay.start_game(screen, FPS, BG, COORDINATES, mode=2)
        pygame.display.update()


def setting_screen(screen):
    screen.fill((51, 255, 220))
    game_font = pygame.font.SysFont("Comic Sans MS", 30)
    text_surface = game_font.render("Main Menu", False, red)
    screen.blit(text_surface, (220, 120))  # draws image on to another, in this case text on the screen
    setting_box(screen, "Comic Sans MS", "One Player", 210, 250, 170, 40, 222, 245)
    setting_box(screen, "Comic Sans MS", "Two Player", 210, 300, 170, 40, 222, 295)


def setting_box(screen, font, text, x, y, width, height, a, b):
    pygame.draw.rect(screen, red, (x, y, width, height), width=3)
    game_font = pygame.font.SysFont(font, 30)
    text_surface = game_font.render(text, False, red)
    screen.blit(text_surface, (a, b))