def solution(user_id, banned_id):
    answer = [0] * len(user_id)
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if len(banned_id[i]) == len(user_id[j]):
                for z in range(len(user_id[j])):
                    if user_id[j][z] == banned_id[i][z] :
                        answer[j] += 1
                if list(set(banned_id[i]))[0] == "*":

    return user_id, answer


if __name__ == "__main__":
    user_id =["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]
    print(solution(user_id, banned_id))