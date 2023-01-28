#
# @lc app=leetcode.cn id=1290 lang=python3
#
# [1290] 二进制链表转整数
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
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ret = 0
        while head:
            ret <<= 1
            ret |= head.val
            head = head.next
        return ret
# @lc code=end

print(Solution().getDecimalValue(
    ListNode(1, ListNode(0, ListNode(1)))
))