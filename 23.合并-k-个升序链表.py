#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
from typing import List, Optional
import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        pq = [i for i in lists if i is not None]
        heapq.heapify(pq)
        head = ListNode()
        tail = head
        while pq:
            tail.next = heapq.heappop(pq)
            tail = tail.next
            if tail.next is not None: heapq.heappush(pq, tail.next)
        tail.next = None
        return head.next
# @lc code=end

