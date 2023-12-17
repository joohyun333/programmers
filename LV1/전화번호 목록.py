# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution1(phone_book):
    phoneHash = set(phone_book);
    for phone in phone_book:
        compareStr = ""
        for phoneStr in phone:
            compareStr += phoneStr
            if compareStr != phone and compareStr in phoneHash:
                return False
    return True

def solution2(phone_book):
    phoneHash = set(phone_book);
    for phone in phone_book:
        compareStr = ""
        for phoneStr in phone:
            compareStr += phoneStr
            if compareStr != phone and compareStr in phoneHash:
                return False
    return True

if __name__ == "__main__":
    phone_book = ["119", "97674223", "1195524421"]
    # phone_book = ["123","456","789"]
    # phone_book = ["12","123","1235","567","88"]
    solution1(phone_book)
    solution2(phone_book)
