def circle(x, y, r):
    board = [[0]*81 for _ in range(25)]
    for X in range(0,81):
        for Y in range(0, 25):
            if (((X-x)**2) + ((Y - y)**2)) <= r**2:
                board[X][Y] = "*"
    for i in board:
        for j in i :
            print(j, end=" ")
        print()
    return

if __name__ == "__main__":
     print(circle(10,10,10))