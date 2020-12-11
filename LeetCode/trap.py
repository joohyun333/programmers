from builtins import str
from typing import List
def trap(height: List[int]) -> int:
    stack = []
    volume = 0
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            # print(stack)
            top = stack.pop()
            if not len(stack):
                break
            print(stack)
            distnace = i - stack[-1] -1
            waters = min(height[i], height[stack[-1]]) - height[top]
            volume += distnace * waters
            print(i, distnace, waters, volume)
        stack.append(i)
    return volume
if __name__ == "__main__":
    height = [4,2,0,3,2,5]
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(height))