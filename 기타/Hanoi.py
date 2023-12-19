def tanoi(s, d, e, n):
    if n <=0:
        return
    tanoi(s,e, d, n-1)
    print(n, s, d)
    tanoi(e, d, s, n-1)
tanoi("s","d","e", 4)