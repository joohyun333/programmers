from typing import List
import collections
import string
def mostCommonWord(paragraph: str, banned: List[str]) -> str:

    strs = ''.join([i.lower() for i in paragraph if i not in string.punctuation])
    result = collections.Counter(strs.split()).most_common()
    for results in result:
        if results[0] == banned[0]:
            pass
        else:
            return results[0]
    return result
if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(mostCommonWord(paragraph.lower(),banned))