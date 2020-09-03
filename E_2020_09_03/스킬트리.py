#https://programmers.co.kr/learn/courses/30/lessons/49993#fnref1

def solution(skill, skill_trees):
    answer = [] #s의 모음들
    s = [] #skilltree내에 있는 skill의 알파벳만 넣는 리스트(answer에 넣기 위해 잠시 모아둠)
    result = 0 # (skill 순서대로 넣은 skilltree) 와 (skill에 포함되지 않은 알파벳으로만 이루어진 skilltree)
    bask = 0
    # skill_trees에 포함된 요소중 skill에 포함되지 않은 알파벳으로만 이루어진 경우,
    # 어떤 스킬을 넣어도 상관없으므로, bask 랑 skill에 포함되지 않은 알파벳 숫자랑 같으면 result += 1을 추가한다.
    # (이것떔에 많이 헤맴.. 역시 testcase만 믿지 말자..)
    for i, e in enumerate(skill_trees):
        for j in e:
            if j in skill:
                s.append(j)
            else:
                bask += 1
                print(bask, len(e))
                if bask == len(e):
                    result += 1
        bask = 0
        answer.append(s[:])
        s.clear()

    skill_list = [] # skill의 알파벳으로 만들수 있는 규칙에 입각한 skill의 경우의 case들
    skill_list.append(skill)
    for i in range(1,len(skill)):
        skill_list.append(skill[:-i])

    # anwser 에 skill_list 가 있으면 result += 1
    for i,e in enumerate(answer):
        if ''.join(e) in skill_list:
            print(''.join(e))
            result += 1
    return result

if __name__ == "__main__":
    skill ="CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    # skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "AQWER"]
    print(solution(skill, skill_trees))