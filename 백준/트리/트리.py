# https://www.acmicpc.net/problem/1068
n = int(input())
d = list(map(int, input().split()))
child_nodes = {}
for i in range(-1, n):
    child_nodes[i] = []
for i in range(n):
    child_nodes[d[i]].append(i)
remove_n = int(input())
child_node = child_nodes.get(d[remove_n])
child_node.remove(remove_n)


answer = 0

def search_leaf(node):
    global answer
    if child_nodes.get(node):
        for c in child_nodes[node]:
            search_leaf(c)
    else:
        if node != -1:
            answer += 1
        return

search_leaf(-1)
print(answer)

