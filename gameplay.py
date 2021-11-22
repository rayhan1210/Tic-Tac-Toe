import pygame
# import sys


class Gameplay:
    def __init__(self):
        self.loop = True

    def start_game(self, mid_area, mid_left, mid_right, top_area, top_right, top_left, btm_area, btm_right, btm_left):

        while self.loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.loop = False
                    # sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if mid_area.collidepoint(event.pos):  # if mouse is inside the area use collidepoint to check that
                        print("in mid")
                        # pygame.draw.line(screen, red, draw_x[0], draw_x[1], width=3)
                        # pygame.draw.line(screen, red, draw_x[2], draw_x[3], width=3)
                    elif mid_left.collidepoint(event.pos):
                        print("In mid left")
                    elif mid_right.collidepoint(event.pos):
                        print("in mid right")
                    elif top_area.collidepoint(event.pos):
                        print("In top ")
                    elif top_right.collidepoint(event.pos):
                        print("in top right")
                    elif top_left.collidepoint(event.pos):
                        print("In top left")
                    elif btm_area.collidepoint(event.pos):
                        print("In btm")
                    elif btm_right.collidepoint(event.pos):
                        print("in btm right")
                    elif btm_left.collidepoint(event.pos):
                        print("In btm left")
                    else:
                        print("error")
            pygame.display.flip()


