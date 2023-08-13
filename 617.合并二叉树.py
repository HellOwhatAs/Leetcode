#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is root2 is None: return None
        if root1 is None: return root2
        if root2 is None: return root1
        return TreeNode(root1.val + root2.val, self.mergeTrees(root1.left, root2.left), self.mergeTrees(root1.right, root2.right))
# @lc code=end

