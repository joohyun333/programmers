# 트라이의 노드
import collections


class TriNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TriNode)


class Trie:
    def __init__(self):
        self.root = TriNode()

    # 단어삽입
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # 단어 존재 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    # 문자열로 시작 단어 존재 여부 판별
    def startWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
