import pygame
import sys
import structure


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    game_window = structure
    game_window.display_window(screen)


if __name__ == "__main__":
    main()
