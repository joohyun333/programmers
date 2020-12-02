# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s:str) -> int:
    if len(s) < 2:
        return len(s)
    string = [s[0:i] for i in range(1,(len(s)//2)+1)]
    answer = []
    print(string)
    for i in range(len(string)):
        num = 0
        result=[]
        for j in range(0,len(s),len(string[i])):
            print(j)
            if string[i] == s[j:j+len(string[i])]:
                num += 1
            else:
                result.append(num)
                string[i] = s[j:j+len(string[i])]
                num = 1
        result.append(num)
        print(result)
        index = [i for i in result if i>1]
        resultstr = s + ''.join(map(str,index))
        j = (i+1) * sum([flex-1 for flex in index])
        answer.append(len(resultstr)-j)
    return min(answer)

if __name__ == "__main__":
    s = "aabbaccc"

    print(solution(s))