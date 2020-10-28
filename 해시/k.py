from functools import reduce
a = [1,2]
for i in range(1,len(a)+1):
    print(reduce(lambda x,y : x*y, a[0:i]))
