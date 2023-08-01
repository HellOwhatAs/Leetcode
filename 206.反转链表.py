#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def func(self, head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return tail
        head.next, tail, head = tail, head, head.next
        return self.func(head, tail)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.func(head, None)
# @lc code=end

print(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))