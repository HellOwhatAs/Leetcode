#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.val}, {repr(self.next)})'
# @lc code=start
from typing import Optional
from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        while head is not None:
            q.append(head)
            head = head.next
        while True:
            if not q: break
            q.popleft().next = q[-1] if len(q) > 1 else None
            if not q: break
            q.pop().next = q[0] if len(q) > 1 else None
# @lc code=end

tmp = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
Solution().reorderList(tmp)
print(tmp)