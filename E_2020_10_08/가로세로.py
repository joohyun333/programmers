def solution(arr):
    x = len(arr)//2
    y = len(arr)
    print(arr)
    a= [[i[0:x] for i in arr[0:x]],[i[x:y] for i in arr[0:x]],[i[0:x] for i in arr[x:y]],[i[x:y] for i in arr[x:y]]]
    a_m = [set(j for i in a[z] for j in i) for z in range(len(a))]
    result = []
    for i in range(len(a_m)):
        if len(a_m[i]) == 1:
            result.append(a.pop(i))
        else:
            solution(a_m[i])
    return a, a_m, result

if __name__ == "__main__":
    arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
    print(solution(arr))