import pygame
import sys
import structure

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


# mid_area = board[1][1]
# mid_left = board[1][0]
# mid_right = board[1][2]

def start_game(screen, FPS, mid_area, mid_left, mid_right, top_area, top_right, top_left, btm_area, btm_right,
               btm_left):
    # checkBoard(board)
    player = 0
    value = True
    clock = pygame.time.Clock()
    while value:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                player = changePlayer(player)
                if mid_area.collidepoint(event.pos):  # if mouse is inside the area use collide point to check that
                    print("in mid")
                    game_char(player, screen, 0, 120, 1, 1, board)
                    print(board[1][1])
                elif mid_left.collidepoint(event.pos):
                    print("In mid left")
                    game_char(player, screen, -135, 120)
                elif mid_right.collidepoint(event.pos):
                    print("in mid right")
                    game_char(player, screen, 135, 120)
                elif top_area.collidepoint(event.pos):
                    print("In top ")
                    game_char(player, screen, 0, 0)
                elif top_left.collidepoint(event.pos):
                    print("in top left")
                    game_char(player, screen, -135, 0)
                elif top_right.collidepoint(event.pos):
                    print("In top right")
                    game_char(player, screen, 135, 0)
                elif btm_area.collidepoint(event.pos):
                    print("In btm")
                    game_char(player, screen, 0, 240)
                elif btm_right.collidepoint(event.pos):
                    print("in btm right")
                    game_char(player, screen, 135, 240)
                elif btm_left.collidepoint(event.pos):
                    print("In btm left")
                    game_char(player, screen, -135, 240)
                else:
                    print("error")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    structure.main_menu(screen)
                    value = False
        pygame.display.update()


def checkBoard(board, i, j):
    print(f"board: {board[i][j]}")


def game_char(player, screen, x, y, i, j, b):
    if player == 1:
        structure.draw_cross(screen, x, y)
        b[i][j] = 1
        # print(b[i][j])
    if player == 2:
        structure.draw_circle(screen, x, y)
        b[i][j] = 2


def changePlayer(player):
    if player == 0:
        player = 1
    elif player == 1:
        player = 2
    else:
        player = 1
    return player
