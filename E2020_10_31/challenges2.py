import string
def solution(encrypted_text : str, key : str, rotation: int) -> str:
    n = rotation % len(encrypted_text)
    encrypted_text = encrypted_text[n:] + encrypted_text[:n]
    values = [[],[],[]]
    for i in encrypted_text:
        values[0].append(string.ascii_lowercase.index(i)+1)
    for j in key:
        values[1].append(string.ascii_lowercase.index(j)+1)
    for i , j in zip(values[0], values[1]):
        values[2].append(string.ascii_lowercase[i-j-1])
    return ''.join(map(str,values[2]))

if __name__ == "__main__":
    encrypted_text, key, rotation = "h", "e", -1
    print(solution(encrypted_text, key, rotation))