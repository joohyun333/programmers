# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        a = head
        b = head
        while a and b and b.next:
            a = a.next
            b = b.next.next
            if a == b:
                return True
        return False



