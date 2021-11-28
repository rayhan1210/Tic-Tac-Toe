import pygame
import sys
import structure
import random

ROW = 3
COL = 3
LINE_COLOR = (74, 171, 155)
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


# board = numpy.zeros((ROW, COL))
# if player 1 draw x else draw 0


# check board has empty slot or not
def check_board(row, col):
    # if board[row][col] == 0:
    #     return True
    # else:
    return board[row][col] == 0


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


def game_win_check(game_board, player, screen):
    # check vertical
    for row in range(ROW):
        col = 0
        if game_board[row][0] == player and game_board[row][1] == player and game_board[row][2] == player:
            structure.draw_vertical_line(screen, row, col)
            return True

    # check horizontal
    for col in range(COL):
        row = 0
        if game_board[row][col] == player and game_board[row + 1][col] == player and game_board[row + 2][col] == player:
            structure.draw_horizontal_line(screen, row, col)
            return True

    # check ascending diagonal
    if game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player:
        structure.draw_asc_diagonal(screen, 0, 0, 2, 2)
        return True
    if game_board[0][2] == player and game_board[1][1] == player and game_board[2][0] == player:
        structure.draw_asc_diagonal2(screen, 0, 2, 2, 0)
        return True


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
    board_full_length = 9
    value, game_ended = True, False
    clock = pygame.time.Clock()
    reset_board()
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
                if mode == 1:
                    if check_board(row, col) and board_full_length > 0:
                        board[row][col] = 1
                    board_full_length -= 1
                    if game_win_check(board, player, screen):
                        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                    else:
                        player = 2
                elif mode == 2:
                    two_player = mode_two(row, col, two_player)
                    if game_win_check(board, two_player, screen):
                        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                    # board_full_length -= 1
            if mode == 1 and player == 2 and board_full_length > 0:
                bot_row, bot_col = randColRow()
                if check_board(bot_row, bot_col):
                    board[bot_row][bot_col] = 2
                    board_full_length -= 1
                else:
                    av = True
                    while not check_board(bot_row, bot_col) and av:
                        bot_row, bot_col = randColRow()
                        if check_board(bot_row, bot_col):
                            board[bot_row][bot_col] = 2
                            board_full_length -= 1
                            av = False
                if game_win_check(board, player, screen):
                    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                else:
                    player = 1
            draw_game_figure(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_board()
                    player, two_player = 1, 0
                    board_full_length = 9
                    structure.draw_game_outlier(screen, BG, LINE_COLOR, COORDINATES)
                    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                if event.key == pygame.K_ESCAPE:
                    screen.fill(BG)
                    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                    structure.main_menu(screen)
                    value = False
        pygame.display.update()


def randColRow():
    bot_row = random.randint(0, 2)
    bot_col = random.randint(0, 2)
    return bot_row, bot_col


def reset_board():
    for row in range(ROW):
        for col in range(COL):
            board[row][col] = 0
