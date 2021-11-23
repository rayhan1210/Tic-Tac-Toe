import pygame
import sys
import structure


def start_game(screen, mid_area, mid_left, mid_right, top_area, top_right, top_left, btm_area, btm_right, btm_left):
    print("in start_game")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # self.loop = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mid_area.collidepoint(event.pos):  # if mouse is inside the area use collide point to check that
                    print("in mid")
                    # structure.draw_gamechar_x(screen, 0, 120)
                    structure.draw_circle(screen, 0, 120)
                elif mid_left.collidepoint(event.pos):
                    print("In mid left")
                    # structure.draw_gamechar_x(screen, -135, 120)
                    structure.draw_circle(screen, -130, 120)
                elif mid_right.collidepoint(event.pos):
                    print("in mid right")
                    # structure.draw_gamechar_x(screen, 135, 120)
                    structure.draw_circle(screen, 130, 120)
                elif top_area.collidepoint(event.pos):
                    print("In top ")
                    # structure.draw_gamechar_x(screen, 0, 0)
                    structure.draw_circle(screen, 0, 0)
                elif top_left.collidepoint(event.pos):
                    print("in top left")
                    # structure.draw_gamechar_x(screen, -135, 0)
                    structure.draw_circle(screen, -130, 0)
                elif top_right.collidepoint(event.pos):
                    print("In top right")
                    # structure.draw_gamechar_x(screen, 135, 0)
                    structure.draw_circle(screen, 130, 0)
                elif btm_area.collidepoint(event.pos):
                    print("In btm")
                    # structure.draw_gamechar_x(screen, 0, 240)
                    structure.draw_circle(screen, 0, 240)
                elif btm_right.collidepoint(event.pos):
                    print("in btm right")
                    # structure.draw_gamechar_x(screen, 135, 240)
                    structure.draw_circle(screen, 130, 240)
                elif btm_left.collidepoint(event.pos):
                    print("In btm left")
                    # structure.GameStructure().draw_gamechar_x(screen, -135, 240)
                    structure.draw_circle(screen, -130, 240)
                else:
                    print("error")
        pygame.display.flip()
