import re
def isMatch(s: str, p: str) -> bool:
    return True if re.fullmatch(p,s) else False
s = "aa"
p = "a"
print(isMatch(s,p))