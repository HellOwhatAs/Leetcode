#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        tmp, head.next = head.next, self.swapPairs(head.next.next)
        tmp.next = head
        return tmp
# @lc code=end

