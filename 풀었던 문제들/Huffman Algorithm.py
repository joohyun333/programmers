import collections, heapq

content_file = open("chess.txt", "r")
line = content_file.read()
content_file.close()
content = []
for i in line:
    if i.isalpha():
        content.append(i)

content_frequency = []
for i, e in collections.Counter(content).items():
    heapq.heappush(content_frequency, (e, 1, i))


content_frequency_dict = collections.defaultdict(list) # 트리
root, root_frequency = "", 0 # 루트노드, 루트노드의 빈도수 == 총 문자열 길이

while len(content_frequency) > 1:
    string_1 = heapq.heappop(content_frequency)
    string_2 = heapq.heappop(content_frequency)
    frequency, ascii_num, string = string_1[0] + string_2[0], string_1[1] + string_2[1], string_1[2] + string_2[2]
    if root_frequency < frequency: # 루트 노드 update
        root_frequency = frequency
        root = string
    content_frequency_dict[string].append(string_1[2])
    content_frequency_dict[string].append(string_2[2])

    heapq.heappush(content_frequency, (frequency, ascii_num, string))
    # (frequency:빈도수, ascii_num:트리의 노드 수(String변수 길이) , string: 트리(보기쉽게 문자열형태로 print))
def dfs(s, bits):
    if len(s) == 1:
        return result[s].append(bits)
    dfs(content_frequency_dict[s][0], bits + "0")
    dfs(content_frequency_dict[s][1], bits + "1")


result = collections.defaultdict(list)
dfs(root, "")
print(result)

f = open("test1.txt", "w")
for i in content:
    a = bin(ord(i))[2:] # 기존 아스키코드 이진수
    f.write(a)
f.close()

f = open("test2.txt", "w")
for i in content:
    a = result[i][0] # huffman result값
    f.write(a)
f.close()