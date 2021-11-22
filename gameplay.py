import pygame
# import sys
import structure


class Gameplay:
    def __init__(self):
        self.loop = True

    def start_game(self, screen, mid_area, mid_left, mid_right, top_area, top_right, top_left, btm_area, btm_right, btm_left):
        while self.loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.loop = False
                    # sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if mid_area.collidepoint(event.pos):  # if mouse is inside the area use collide point to check that
                        print("in mid")
                        structure.GameStructure().draw_gamechar_x(screen, 0, 120)
                    elif mid_left.collidepoint(event.pos):
                        print("In mid left")
                        structure.GameStructure().draw_gamechar_x(screen, -135, 120)
                    elif mid_right.collidepoint(event.pos):
                        print("in mid right")
                        structure.GameStructure().draw_gamechar_x(screen, 135, 120)
                    elif top_area.collidepoint(event.pos):
                        print("In top ")
                        structure.GameStructure().draw_gamechar_x(screen, 0, 0)
                    elif top_right.collidepoint(event.pos):
                        print("in top left")
                        structure.GameStructure().draw_gamechar_x(screen, -135, 0)
                    elif top_left.collidepoint(event.pos):
                        print("In top right")
                        structure.GameStructure().draw_gamechar_x(screen, 135, 0)
                    elif btm_area.collidepoint(event.pos):
                        print("In btm")
                        structure.GameStructure().draw_gamechar_x(screen, 0, 240)
                    elif btm_right.collidepoint(event.pos):
                        print("in btm left")
                        structure.GameStructure().draw_gamechar_x(screen, -135, 240)
                    elif btm_left.collidepoint(event.pos):
                        print("In btm right")
                        structure.GameStructure().draw_gamechar_x(screen, 135, 240)
                    else:
                        print("error")
            pygame.display.flip()
