import pygame
import sys
import structure
import numpy

ROW = 3
COL = 3
SQUARE = 200
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


# board = numpy.zeros((ROW, COL))
# if player 1 draw x else draw 0


# check board has empty slot or not
def check_board(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False


def change_player(player):
    if player == 0:
        player = 1
    elif player == 1:
        player = 2
    else:
        player = 1
    return player


def draw_game_figure(screen, row, col):
    if board[row][col] == 2:
        draw_o(screen, row, col)
    if board[row][col] == 1:
        draw_x(screen, row, col)


def draw_x(screen, row, col):
    pygame.draw.line(screen, (0, 0, 0), (row * SQUARE + SQUARE / 4, (col * SQUARE) + SQUARE / 4),
                     ((SQUARE * row - SQUARE / 4) + SQUARE, (col * SQUARE - SQUARE / 4) + SQUARE), width=15)
    pygame.draw.line(screen, (0, 0, 0), (row * SQUARE + SQUARE / 4, (col * SQUARE - SQUARE / 4) + SQUARE),
                     ((SQUARE * row - SQUARE / 4) + SQUARE, (col * SQUARE) + 50), width=15)


def draw_o(screen, row, col):
    pygame.draw.circle(screen, (0, 0, 0), (row * SQUARE + SQUARE / 2, (col * SQUARE) + SQUARE / 2), radius=50, width=15)


def draw_horizontal_line(screen, row, col):
    pygame.draw.line(screen, (0,0,0), (row * SQUARE + SQUARE / 4, (col * SQUARE) + SQUARE / 2),
                     ((SQUARE * 3 - SQUARE / 4), (col * SQUARE) + SQUARE / 2), width=15)
    # print("HERE")


def draw_vertical_line(screen, row, col):
    pygame.draw.line(screen, (0,0,0), (row * SQUARE + SQUARE / 4, (col * SQUARE) + SQUARE / 2),
                     (row * SQUARE + SQUARE / 4, (3 * SQUARE) - SQUARE / 2), width=15)


def draw_asc_diagonal(screen, row, col):
    pygame.draw.line(screen, (255, 0, 0), (row * SQUARE + SQUARE / 2, SQUARE / 2),
                     (abs(col * SQUARE - SQUARE / 2), (3 * SQUARE) - SQUARE / 2), width=15)


def draw_dsc_diagonal(screen, row, col):
    pygame.draw.line(screen, (255, 0, 0), (row * SQUARE + SQUARE / 2, (3 * SQUARE) - SQUARE / 2),
                     (abs(row * SQUARE - SQUARE / 2), (3 * SQUARE) + SQUARE / 2), width=15)


def game_win_check(game_board, player, screen):
    # check vertical
    for row in range(ROW):
        col = 0
        if game_board[row][0] == player and game_board[row][1] == player and game_board[row][2] == player:
            draw_vertical_line(screen, row, col)
            return player

    # check horizontal
    for col in range(COL):
        row = 0
        if game_board[row][col] == player and game_board[row + 1][col] == player and game_board[row + 2][col] == player:
            draw_horizontal_line(screen, row, col)
            return player

    # check ascending diagonal
    if game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player:
        draw_asc_diagonal(screen, 0, 3)
        return player
    if game_board[0][2] == player and game_board[1][1] == player and game_board[2][0] == player:
        draw_asc_diagonal(screen, 2, 1)
        return player

    # check descending diagonal
    if game_board[2][2] == player and game_board[1][1] == player and game_board[0][0] == player:
        draw_horizontal_line(screen, 0, 2)
        return player
    if game_board[2][0] == player and game_board[1][1] == player and game_board[0][2] == player:
        draw_horizontal_line(screen, 2, 0)
        return player


def start_game(screen, FPS, BG, COORDINATES):
    player = 0
    value = True
    clock = pygame.time.Clock()
    structure.draw_game_outlier(screen, BG, (74, 171, 155), COORDINATES)
    while value:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                row = int(mouseX // 200)
                col = int(mouseY // 200)
                if check_board(row, col):
                    player = change_player(player)
                    if player == 1:
                        board[row][col] = 1
                    elif player == 2:
                        board[row][col] = 2
                    else:
                        board[row][col] = 0
                    if game_win_check(board, player, screen) == player:
                        # print(f"player {player} wins")
                        value = False
                draw_game_figure(screen, row, col)
        pygame.display.update()
