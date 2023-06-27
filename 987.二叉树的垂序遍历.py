#
# @lc app=leetcode.cn id=987 lang=python3
#
# [987] 二叉树的垂序遍历
#


from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func(self, root: Optional[TreeNode], col: int, depth: int):
        if root is None: return
        self.data[col][depth].append(root.val)
        self.func(root.left, col - 1, depth + 1)
        self.func(root.right, col + 1, depth + 1)
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.data = defaultdict(lambda:defaultdict(list))
        self.func(root, 0, 0)
        return [sum((sorted(self.data[k][k1]) for k1 in sorted(self.data[k].keys())), []) for k in sorted(self.data.keys())]
# @lc code=end

