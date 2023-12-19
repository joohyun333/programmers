def zero_one_kanpsack(cargo):
    capacity = 15
    pack = []
    for i in range(len(cargo)+1):
        pack.append([])
        for c in range(capacity+1):
            print(i, cargo[i-1], pack[i-1], c,c-cargo[i-1][1])
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i-1][1] < c :
                pack[i].append(max(cargo[i-1][0]+pack[i-1][c-cargo[i-1][1]], pack[i-1][c]))
            else:
                pack[i].append(pack[i-1][c])
        print(pack[i])
    return
if __name__ == "__main__":
    cargo = (4,12),(2,1),(10,4),(1,1),(2,2)
    print(zero_one_kanpsack(cargo))