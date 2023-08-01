#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @lc code=start
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def search(self, root: TreeNode, target: TreeNode, trace: List[TreeNode]) -> bool:
        if root is None: return False
        if root is target or self.search(root.left, target, trace) or self.search(root.right, target, trace):
            trace.append(root)
            return True
        return False
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p, path_q = [], []
        self.search(root, p, path_p)
        self.search(root, q, path_q)
        sp = set(path_p)
        for i in path_q:
            if i in sp: return i
        return root
# @lc code=end