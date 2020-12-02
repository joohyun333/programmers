# https://programmers.co.kr/learn/courses/30/lessons/60059
from itertools import product
from typing import List
from copy import deepcopy
def solution(key : List, lock: List) -> bool:
    lock_ = [[0]*(len(key)*2-2+len(lock)) for i in range(len(key)*2-2+len(lock))] #빈공간
    lock_index = list(product(range(len(key)-1,len(key)-1 + len(lock)),range(len(key)-1,len(key)-1 + len(lock)))) #중앙값
    index = list(product(range(len(lock)),range(len(lock)))) # 자물쇠 인덱스
    for i,j in zip(lock_index, index): # 자물쇠 중앙에 넣기
        lock_[i[0]][i[1]] = lock[j[0]][j[1]]
    start_point =list(product(range(len(lock_)-len(key)+1),range(len(lock_)-len(key)+1))) # 열쇠시작지점
    key_index = list(product(range(len(key)),range(len(key)))) # 열쇠 인덱스
    lock_data = deepcopy(lock_)
    for p in range(4): # 열쇠랑 자물쇠 비교
        for s_x,s_y in start_point:
            for k_x,k_y in key_index:
                lock_data[s_x+k_x][s_y+k_y] = int(bin(lock_data[s_x+k_x][s_y+k_y]^key[k_x][k_y]),2)
            if set([lock_data[i][j] for i,j in lock_index]) == {1}:  #조건충족
                return True
            lock_data = deepcopy(lock_)
        key = turn(key)
    return False
def turn(data:List)->List: #90도 회전
    data_ = []
    for i in range(len(data[0])):
        a = []
        for j in range(len(data)-1,-1,-1):
            a.append(data[j][i])
        data_.append(a)
    return data_
if __name__ == "__main__":
    key, lock = [[0,0,0],[1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))