def powerset(s):
    n = len(s)
    masks = [1<<j for j in range(n)]
    for i in range(2**n):
        yield [s[j] for j in range(n) if (masks[j] & i)]


if __name__ == '__main__':
    for elem in powerset([1,2,3,4,5]):
        print (elem)