import pygame
import getpass as gp
import socket
from pprint import pprint
import random
import numpy

SystemUser = gp.getuser()

# pygame.init()
# pygame.display.init()
# window_surface = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
# clock = pygame.time.Clock()
# pygame.display.set_caption("game")
GRID_WIDTH, GRID_HEIGHT = 10, 20

display_board = [
    [0 for _ in range(GRID_WIDTH)]
    for _ in range(GRID_HEIGHT)
]
board = [
    [0 for _ in range(GRID_WIDTH)]
    for _ in range(GRID_HEIGHT)
]
class Piece:
    def __init__(self):
        pass

    i_piece =
    j_piece =
    l_piece =
    o_piece =
    s_piece =
    t_piece =
    z_piece =
    piece_list = [i_piece, j_piece, l_piece, o_piece, s_piece, t_piece, z_piece]


# def add_to_bord(start_x,start_y):
#     x = start_x
#     y = start_y
#
#
#
#     count_x = 0
#     count_y = 0
#     piece_tipe = piece_list[0]
#     Piece_Rotate = piece_tipe[0]
#
#
#     while count_x != 4:
#         board_row = board[count_x]
#         Piece_Row = Piece_Rotate[count_x]
#
#         while count_y != 4:
#             board_cell = board_row[count_y]
#             Piece_cell = Piece_Row[count_y]
#
#             if Piece_cell == 1:
#                 board[x][y] += 1
#             count_y += 1
#             y += 1
#         count_x += 1
#         count_y = 0
#         x += 1
#         y = start_y
#
#
#
#     pprint(board)
#


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                new_width, new_height = event.size
                window_surface = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

        update()
        # clock.tick(60)


def update():
    pygame.display.flip()
    print(pygame.key.get_focused())


if __name__ == "__main__":
    # main()
    # pygame.QUIT()
    #add_to_bord(0,0)
