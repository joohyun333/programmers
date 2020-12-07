from itertools import product
import sys
from collections import defaultdict
from copy import deepcopy
n = int(input())
bamboo= [[-sys.maxsize for i in range(n+1)]]
for i in range(n):
    bamboo.append([-sys.maxsize]+list(map(int, input().split()))+[-sys.maxsize])
bamboo.append([-sys.maxsize for i in range(n+1)])
bamboo_index = list(product(range(1,n+1), range(1,n+1)))
bam_dic = defaultdict(list)
direction = [(-1,0),(1,0),(0,-1),(0,1)]
for x,y in bamboo_index:
    p = [x,y]
    bam_dic[(x,y)].append(p)
    bamboo_ = deepcopy(bamboo)
    while p != []:
        a = [(bamboo_[p[0]+i[0]][p[1]+i[1]],p[0]+i[0],p[1]+i[1]) for i in direction if bamboo_[p[0]][p[1]]<bamboo_[p[0]+i[0]][p[1]+i[1]]]
        if a == []:
            p = []
            break
        else:
            a = sorted(a)[0]
            p = [a[1],a[2]]
            bam_dic[(x,y)].append(p)
print(len(max(bam_dic.values(), key=len)))
# 시간초과