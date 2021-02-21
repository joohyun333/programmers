import math
n = int(input())
tree = [int(input()) for _ in range(n)]
g = tree[1] - tree[0]
for i in range(2, n):
    g = math.gcd(g, tree[i] - tree[i - 1])
answer = (tree[n - 1] - tree[0]) // g + 1 - n
print(answer)