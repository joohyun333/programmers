def solution(rule, A, B):
    num = len(rule)
    key = (i for i in range(num))
    val = (j for j in rule)
    rule_dic = list(zip(key, val))

    aa = ""
    bb = ""
    for a in A:
        for x, y in rule_dic:
            if y == a:
                aa += str(x)
    for b in B:
        for x, y in rule_dic:
            if y == b:
                bb += str(x)

    x = int(aa,num) - int(bb,num)
    y = ""
    while x > 0:
        y = str(x % num) + y
        x //= num

    result = ''
    for i in y:
        result += rule_dic[int(i)][1]
    return result

if __name__ == "__main__":
    # rule = "zothf"
    # A = "otz"
    # B = "hh"

    rule = "ab"
    A = "ba"
    B = "a"
    print(solution(rule,A,B))
    print(solution("lejohyun", "yey", "oon"))