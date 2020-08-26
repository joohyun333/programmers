def merge_sort_seq(seq):
    if len(seq) < 2 :
        return seq
    mid = len(seq) // 2
    left = merge_sort_seq(seq[:mid])
    right = merge_sort_seq(seq[mid:])
    return merge(left, right)

def merge(left, right):
    if not left or not right :
        return left or right
    result = []
    i, j =0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    return result

if __name__ == "__main__":
    inedx = input()
    list_ = list(map(int,input().split()))
    print(" ".join(map(str, merge_sort_seq(list_))) + " ")