def merge_sort_sep(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq)//2
    left = merge_sort_sep(seq[:mid])
    right = merge_sort_sep(seq[mid:])
    # return merge(left, right)
    return left, right

def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    print(result)
    return result

def test_merge():
    seq = [3,5,2,6,8,1,0,3,5,6,2]
    seq_sorted = sorted(seq)
    assert (merge_sort_sep(seq) == seq_sorted)
    print("테스트 통과")

if __name__ == "__main__":
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    print(merge_sort_sep(seq))
    # test_merge()
