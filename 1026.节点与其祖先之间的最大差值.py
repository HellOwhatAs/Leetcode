#
# @lc app=leetcode.cn id=1026 lang=python3
#
# [1026] 节点与其祖先之间的最大差值
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
from typing import Optional, Tuple, List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def func(root: Optional[TreeNode], minmax: Tuple[int, int], ans: List[int]) -> None:
        if root is None: return
        ans[0] = max(ans[0], abs(minmax[0] - root.val), abs(minmax[1] - root.val))
        minmax = (min(minmax[0], root.val), max(minmax[1], root.val))
        Solution.func(root.left, minmax, ans)
        Solution.func(root.right, minmax, ans)
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        Solution.func(root, (root.val, root.val), ans)
        return ans[0]
# @lc code=end

