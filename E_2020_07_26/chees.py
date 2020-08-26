def solution(root):
    rooter = [[0]*(root[0][0]+1)for _ in range(root[0][1]+1)]
    for [i,j]in root[1:]:
        print(i,j)
        rooter[i][j] =1
    return rooter

if __name__ == "__main__":
    root = [[5,5],[2,3],[3,2],[4,3],[4,5],[5,2]]
    print(solution(root))
