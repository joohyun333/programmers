def solution(s:str) -> int:
    result = []
    for i in range(len(s)+1):
        for j in range(i,len(s)):
            result.append(s[i:j+1])
    result_1 = len([j for j in result if len(set(j)) > 1 and len(j) == 2])
    result = [j for j in result if len(set(j)) > 1 and len(j)>2]
    answer = [0] * len(result) #['ba', 'bab', 'baby', 'ab', 'aby', 'by']
    for i, z in enumerate(result):
        for c in range(len(z)-1,0,-1):
            if z[0] != z[c]:
                answer[i] += len(z[0:c])
                break
    return sum(answer)+ result_1

if __name__ == "__main__":
    s = "baby"
    # s = "bbib"
    print(solution(s))