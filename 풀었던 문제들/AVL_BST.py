from binary_tree import NodeBt, BinaryTree

class NodeAVL(NodeBt):
    def __init__(self, value = None, height = 1):
        self.value = value
        self.height = height
        self.left = None
        self.right = None

    def insert(self, value):
        new_node = NodeAVL(value)
        if value < self.value:
            self.left = self.left and self.left.insert(value) or new_node
        elif value > self.value:
            self.right = self.right and self.right.insert(value) or new_node
        else:
            raise Exception("중복 노드를 허용하지 않습니다.")
        return self.rotate(value)

    def