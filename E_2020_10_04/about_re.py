# https://greeksharifa.github.io/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re)/2018/07/21/regex-usage-02-basic/
import re
matchObj = re.findall('\w\W\w', 'a (9_a a')
print(matchObj) # ['a a']
matchObj = re.search('\w\W\w', 'a (9_a a')
print(matchObj) # <re.Match object; span=(5, 8), match='a a'>
matchObj = re.findall(r'\w\b\W\B', 'ab  c d  == = e= =f')
print(matchObj) # ['b ', 'd ', 'e=']
print(re.findall('\A ryan\d\s\Z', ' ryan1 \n ryan2 \n rain1 \n ryan3 ')) #[]
print(re.findall('\A ryan\d\s\Z', ' ryan1 ')) # [' ryan1 ']
print("\\")
print(r"\"",r"\\")
matchObj = re.findall(r'\bone\b|\boneself\b|\bonerous\b', 'oneself is the one thing.')
print(matchObj)
matchObj = re.findall('oneself|one|onerous', 'oneself is the one thing.')
print(matchObj)
b = "aadas"
print(sorted(b))
print(b.s)