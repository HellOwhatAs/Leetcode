#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
from typing import List, Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def func(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0):
        if l1 is not None and l2 is not None:
            return ListNode((l1.val + l2.val + carry) % 10, self.func(l1.next, l2.next, (l1.val + l2.val + carry) // 10))
        if l1 is l2 is None:
            if carry == 0: return None
            return ListNode(carry % 10, self.func(None, None, carry // 10))
        if l1 is None: l1, l2 = l2, l1
        return ListNode((l1.val + carry) % 10, self.func(l1.next, None, (l1.val + carry) // 10))
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.func(l1, l2)
# @lc code=end

