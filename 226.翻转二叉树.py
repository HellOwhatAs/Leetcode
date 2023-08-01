#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
# @lc code=end

