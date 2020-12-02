# https://leetcode.com/problems/valid-parentheses/
def isValid(s: str) -> bool:
    stack = []
    if len(s) <= 1:
        return False
    table = {")": "(", "}": "{", "]": "["}
    for i in s:
        if not stack or table[i] != stack.pop():
            return False
        elif i not in table:
            stack.append(i)
    return len(stack) == 0

if __name__ == "__main__":
    s = "(){}}{"
    print(isValid(s))