# # https://www.acmicpc.net/problem/5904
N: int =int(input())
moo = [0,3,0]
data = []
data.append(moo.copy())
turn = 0
while sum(moo)<N:
    moo[0] = sum(moo)
    moo[1] = moo[1]+1
    moo[2] = moo[0]
    data.append(moo.copy())
def search_m(w,N):
    if N<4:
        if N == 1:return "m"
        else:return "o"
    w_pop = w.pop()
    w_num = [(sum(w_pop[0:i])-N,i) for i in range(1,len(w_pop)+1) if N<=sum(w_pop[0:i])]
    if w_num[0][1] == 2 :
        if w_num[0][0] == w_pop[1]-1:
            return "m"
        elif w_num[0][0] != w_pop[1]-1:
            return "o"
    elif w_num[0][1] == 1 :
        search_m(w, N)
    return search_m(w, N-w_pop[1]-w_pop[2])
print(search_m(data, N))