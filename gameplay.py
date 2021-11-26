import pygame
import sys
import structure
import numpy, random

ROW = 3
COL = 3
# SQUARE = 200
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


def draw_game_figure(screen):
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == 2:
                structure.draw_o(screen, row, col)
            if board[row][col] == 1:
                structure.draw_x(screen, row, col)
    # if board[row][col] == 2:
    #     structure.draw_o(screen, row, col)
    # if board[row][col] == 1:
    #     structure.draw_x(screen, row, col)


def game_win_check(game_board, player, screen):
    # check vertical
    for row in range(ROW):
        col = 0
        if game_board[row][0] == player and game_board[row][1] == player and game_board[row][2] == player:
            structure.draw_vertical_line(screen, row, col)
            return player

    # check horizontal
    for col in range(COL):
        row = 0
        if game_board[row][col] == player and game_board[row + 1][col] == player and game_board[row + 2][col] == player:
            structure.draw_horizontal_line(screen, row, col)
            return player

    # check ascending diagonal
    if game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player:
        structure.draw_asc_diagonal(screen, 0, 3)
        return player
    if game_board[0][2] == player and game_board[1][1] == player and game_board[2][0] == player:
        structure.draw_asc_diagonal(screen, 2, 1)
        return player

    # check descending diagonal
    if game_board[2][2] == player and game_board[1][1] == player and game_board[0][0] == player:
        structure.draw_horizontal_line(screen, 0, 2)
        return player
    if game_board[2][0] == player and game_board[1][1] == player and game_board[0][2] == player:
        structure.draw_horizontal_line(screen, 2, 0)
        return player


def mode_one(player, row, col):
    if check_board(row, col):
        if player == 1:
            board[row][col] = 1
        else:
            board[row][col] = 0
        # player = 2


def mode_two(row, col, two_player):
    if check_board(row, col):
        two_player = change_player(two_player)
        if two_player == 1:
            board[row][col] = 1
        elif two_player == 2:
            board[row][col] = 2
    return two_player


def start_game(screen, FPS, BG, COORDINATES, mode):
    player, two_player = 1, 0
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
                if mode == 2:
                    two_player = mode_two(row, col, two_player)
                    draw_game_figure(screen, row, col)
                if mode == 1:
                    mode_one(player, row, col)
                    player = 2
            if mode == 1:
                bot_row = random.randint(0, 2)
                bot_col = random.randint(0, 2)
                if player == 2 and check_board(bot_row, bot_col):
                    board[bot_row][bot_col] = 2
                    player = 1
            if game_win_check(board, player, screen) == player:
                value = False
            draw_game_figure(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_board()
                    screen.fill(BG)
                    structure.draw_game_outlier(screen, BG, (74, 171, 155), COORDINATES)
                    print(board)
                if event.key == pygame.K_ESCAPE:
                    screen.fill(BG)
                    structure.main_menu(screen)
                    value = False
                    # value = False
        pygame.display.update()


def reset_board():
    for row in range(ROW):
        for col in range(COL):
            board[row][col] = 0