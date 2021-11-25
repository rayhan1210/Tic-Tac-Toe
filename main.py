import pygame
import sys
import structure, gameplay

WIDTH = 600
HEIGHT = 600
FPS = 60
BG = (51, 255, 220)
RECT_G = (210, 200, 170, 40)
BLACK = (0,0,0)
COORDINATES = [
    (200, 0), (200, 600),
    (400, 0), (400, 600),
    (0, 200), (600, 200),
    (0, 400), (600, 400)
]


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG)
    structure.main_menu(screen)
    text_x, text_y = 210, 200
    clock = pygame.time.Clock()
    start = 0
    value = True
    while value:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                value = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(RECT_G).collidepoint(event.pos):
                    gameplay.start_game(screen, FPS, BG, COORDINATES)

        pygame.display.update()


if __name__ == "__main__":
    main()
