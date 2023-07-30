#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = set()
        while head is not None:
            if id(head) in d: return head
            d.add(id(head))
            head = head.next
        
# @lc code=end

