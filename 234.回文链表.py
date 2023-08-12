#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val) + (f' {repr(self.next)}' if self.next else '')
# @lc code=start
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    @staticmethod
    def ListNodeLength(head: Optional[ListNode]) -> int:
        ret = 0
        while head is not None:
            head = head.next
            ret += 1
        return ret

    @staticmethod
    def nthListNode(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        for _ in range(n):
            head = head.next
        return head
    
    @staticmethod
    def reverseListNode(head: Optional[ListNode]) -> Optional[ListNode]:
        ret = None
        while head is not None:
            tmp = head.next
            head.next = ret
            ret = head
            head = tmp
        return ret
    
    @staticmethod
    def eqListNode(head1: Optional[ListNode], head2: Optional[ListNode]) -> bool:
        while head1 is not None and head2 is not None:
            if head1.val != head2.val: return False
            head1, head2 = head1.next, head2.next
        return head1 is head2 is None

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = self.ListNodeLength(head)
        if n == 1: return True
        tmp = self.nthListNode(head, n // 2 - 1)
        head2 = tmp.next.next if n & 1 else tmp.next
        tmp.next = None
        head2 = self.reverseListNode(head2)
        return self.eqListNode(head, head2)
        
# @lc code=end

l = ListNode
print(Solution().isPalindrome(l(1, l(0, l(1)))))
print(Solution().isPalindrome(l(1, l(0, l(0, l(1))))))