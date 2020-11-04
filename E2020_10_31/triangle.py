def position(x, y, r):
    board = [[0]*81 for _ in range(60)]
    for i in range(x, x+r):
        for j in range(y, y+r):
            board[i][j] = "*"

    for i in board:
        for j in i :
            print(j, end=" ")
        print()
    return

# def triangle(r):
#     for i in range(r):
#         print("*")
#     return

if __name__ == "__main__":
     print(position(50,15,5))