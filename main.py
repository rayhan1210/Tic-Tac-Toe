import pygame

import gameplay,  settings, structure

WIDTH = 600
HEIGHT = 600
FPS = 60
BG = (70, 206, 188)
RECT_S = (210, 250, 170, 40)
BLACK = (0, 0, 0)
COORDINATES = [
    (200, 0), (200, 600),
    (400, 0), (400, 600),
    (0, 200), (600, 200),
    (0, 400), (600, 400)
]
mode = 2
logo = pygame.image.load("tictactoe.JPG")
pygame.display.set_icon(logo)
pygame.display.set_caption("TIC TAC TOE")


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG)
    structure.main_menu(screen)
    clock = pygame.time.Clock()
    rect_g = (210, 200, 170, 40)
    value = True
    while value:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                value = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(rect_g).collidepoint(event.pos):
                    gameplay.start_game(screen, FPS, BG, COORDINATES, mode)
                if pygame.Rect(RECT_S).collidepoint(event.pos):
                    settings.setting(screen, FPS, BG, COORDINATES)

        pygame.display.update()


if __name__ == "__main__":
    main()
