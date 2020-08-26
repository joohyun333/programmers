def solution(name):
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    answer = []
    alpha_n = len(alpha)
    for i in enumerate(alpha):
        for j in name:
            if i[1] == j:
                if i[0] > (alpha_n // 2)-1:
                    answer.append((alpha_n+1) - i[0]-1)
                else:
                    answer.append(i[0])
    result = sum(answer) + len(name) -1
    if "A" in name :
        result -= 1
    return result

if __name__ == "__main__":
    name = "JEROEN"
    print(solution(name))