#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
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
    def merge(self, tail: ListNode, l1: Optional[ListNode], l2: Optional[ListNode]) -> None:
        if l1 is l2 is None: return
        if l1 is None:
            tail.next = l2
            return
        if l2 is None:
            tail.next = l1
            return
        if l1.val > l2.val: l1, l2 = l2, l1
        tail.next, l1 = l1, l1.next
        self.merge(tail.next, l1, l2)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        self.merge(head, list1, list2)
        return head.next
# @lc code=end

