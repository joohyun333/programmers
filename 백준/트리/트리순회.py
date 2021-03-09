import collections, sys
N = int(input())
tree = collections.defaultdict(list)
for i in range(N):
    parent, left, right = map(str, input().split())
    tree[parent].append(left)
    tree[parent].append(right)
def preorder(a,discoverd=[]):
    discoverd.append(a)
    if a in tree:
        if tree[a][0] not in discoverd:
            preorder(tree[a][0])
        if tree[a][1] not in discoverd:
            preorder(tree[a][1])
    return ''.join(discoverd).replace(".","")
def inorder(a, discoverd = []):
    if a in tree:
        if tree[a][0] not in discoverd:
            inorder(tree[a][0])
        discoverd.append(a)
        if tree[a][1] not in discoverd:
            inorder(tree[a][1])
    return ''.join(discoverd).replace(".", "")
def postorder(a, discoverd = []):
    if a in tree:
        if tree[a][0] not in discoverd:
            postorder(tree[a][0])
        if tree[a][1] not in discoverd:
            postorder(tree[a][1])
        discoverd.append(a)
    return ''.join(discoverd).replace(".", "")
print(preorder("A"))
print(inorder("A"))
print(postorder("A"))