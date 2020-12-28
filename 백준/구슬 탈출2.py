# # https://www.acmicpc.net/problem/13460
# import collections
# import itertools
# N, M = map(int, input().split())
# board = []
# R_spot, B_spot, O_spot = (0,0), (0,0), (0,0)
# for i in range(N):
#     board.append(input().split())
# maps = collections.defaultdict(list)
# move = [[-1,0],[0,-1],[0,+1],[+1,0]]
# board_index = list(itertools.product(range(N),range(M)))
# for board_x, board_y in board_index:
#     if board[board_x][0][board_y] != "#":
#         for x, y in move:
#             if board[board_x + x][0][board_y + y] != "#":
#                 maps[(board_x, board_y)].append((board_x + x, board_y + y))
#     if board[board_x][0][board_y] == "R":
#         R_spot = (board_x, board_y)
#     elif board[board_x][0][board_y] == "B":
#         B_spot = (board_x, board_y)
#     elif board[board_x][0][board_y] == "O":
#         O_spot = (board_x, board_y)
# def dfs(spot):
#     discovered = []
#     stack = [spot]
#     while stack:
#         v = stack.pop()
#         if v not in discovered:
#             discovered.append(v)
#             for i in maps[v] :
#                 if i == O_spot:
#                     discovered.append(i)
#                     return discovered
#                 elif i not in discovered and i not in stack:
#                     stack.append(i)
#                 # elif maps[i]
#     return discovered
# print(maps)
# print(dfs(R_spot))

