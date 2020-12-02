def quicksort(A,lo,hi):
    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot-1)
        quicksort(A, pivot+1, hi)

def partition(lo, hi):
    pivot = A[hi]
    left = lo
    print(lo, left)
    for right in range(lo, hi):
        if A[right] < pivot:
            A[left], A[right] = A[right], A[left]
            left += 1
    A[left], A[hi] = A[hi], A[left]
    return left


A = [2,8,7,1,3,5,6,4]
print(quicksort(A,A[0], len(A)-1))
