#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
from typing import List, Optional, Tuple
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, l: Optional[ListNode]) -> int:
        return 0 if l is None else 1 + self.length(l.next)
    
    def add(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Tuple[Optional[ListNode], int]:
        if l1 is l2 is None: return None, 0
        tmp, carry = self.add(l1.next, l2.next)
        val = l1.val + l2.val + carry
        return ListNode(val % 10, tmp), val // 10

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length1, length2 = self.length(l1), self.length(l2)
        if length1 < length2:
            l1, l2, length1, length2 = l2, l1, length2, length1
        for _ in range(length1 - length2):
            l2 = ListNode(0, l2)
        ret, carry = self.add(l1, l2)
        if carry != 0:
            ret = ListNode(carry, ret)
        return ret
        
# @lc code=end

