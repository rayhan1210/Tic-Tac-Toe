import pygame
import sys

pygame.init()
size = max_width, max_height = 600, 500
speed = [1, 1]
black = 0, 0, 0
red = 255, 0, 0
teal = 	(0,128,128)
screen = pygame.display.set_mode(size)
# (x, y)
pos = [
    (220, 60), (220, 420),
    (350, 60), (350, 420),
    (90, 180), (480, 180),
    (90, 300), (480, 300)
]

# mid_area:
#   x1 = 220 y1 = 180
#   x2 = 350 y2 = 180
#   x3 = 220 y3 = 300
#   x4 = 350 y4 = 300

mid_area = pygame.Rect(220, 180, 130, 120)
mid_right = pygame.Rect(350, 180, 130, 120)
mid_left = pygame.Rect(90, 180, 130, 120)

top_area = pygame.Rect(220, 60, 130, 120)
top_left = pygame.Rect(350, 60, 130, 120)
top_right = pygame.Rect(90, 60, 130, 120)

btm_area = pygame.Rect(220, 300, 130, 120)
btm_left = pygame.Rect(350, 300, 130, 120)
btm_right = pygame.Rect(90, 300, 130, 120)


draw_x = [
    [230, 80], [340, 160],
    [340, 80], [230, 160]
]

# draw outline
pygame.draw.line(screen, red, pos[0], pos[1], width=3)
pygame.draw.line(screen, red, pos[2], pos[3], width=3)
pygame.draw.line(screen, red, pos[4], pos[5], width=3)
pygame.draw.line(screen, red, pos[6], pos[7], width=3)



# draw x
pygame.draw.line(screen, red, draw_x[0], draw_x[1], width=3)
pygame.draw.line(screen, red, draw_x[2], draw_x[3], width=3)
# pygame.draw.line(screen, red, pos[2], pos[3], width=3)
# pygame.draw.line(screen, red, pos[4], pos[5], width=3)
# pygame.draw.line(screen, red, pos[6], pos[7], width=3)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event.type)
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if mid_area.collidepoint(event.pos): # if mouse is inside the area use collidepoint to check that
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

