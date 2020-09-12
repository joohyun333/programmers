# https://programmers.co.kr/tryouts/16422/challenges #카카오 1번문제

import string
def solution(new_id):
    new_id = list(new_id.lower())
    check_list = string.ascii_lowercase+string.digits+"."+"-"+"_"
    new_id2 = []
    for i , e in enumerate(new_id):
        if e in check_list:
            new_id2.append(e)
    new_id = []
    while len(new_id2) != 0:
        if new_id[-1:] == ["."] and new_id2[0] == ".":
            new_id2.pop(0)
        else:
            new_id.append(new_id2.pop(0))

    new_id = ("".join(new_id)).strip(".")

    if new_id == "":
        new_id += "a"

    if len(new_id) >= 16:
        new_id = new_id[0:15]
        new_id = ("".join(new_id)).strip(".")

    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]

    return new_id

if __name__ ==  "__main__":
    new_id = 	"...!@BaT#*..y.abcdefghijklm"
    print(solution(new_id))