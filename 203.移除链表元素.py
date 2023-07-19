#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
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
from typing import Optional
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None: return None
        if head.val == val: return self.removeElements(head.next, val)
        head.next = self.removeElements(head.next, val)
        return head
# @lc code=end

