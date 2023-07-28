#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = set()
        while head:
            if id(head) in d: return True
            d.add(id(head))
            head = head.next
        return False
        
# @lc code=end

