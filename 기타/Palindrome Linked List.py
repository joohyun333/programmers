#https://leetcode.com/problems/palindrome-linked-list/
from typing import Deque
from collections import deque
class ListNode:
    def __init__(self, val=[1,2,1], next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next :
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
if __name__ == "__main__":
    head = [1,2]
    print(Solution.isPalindrome(head))