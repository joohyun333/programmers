import collections
a = collections.defaultdict()
for i in range(5):
    a[i] = []
for i in a:
    if a[i]:
        print(a[i])
