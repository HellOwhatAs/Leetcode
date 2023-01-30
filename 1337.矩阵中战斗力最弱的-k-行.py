#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 矩阵中战斗力最弱的 K 行
#

# @lc code=start
from typing import List
class Solution:
    @staticmethod
    def rev_bisect_left(a, x, lo=0, hi=None):
        if lo < 0: raise ValueError('lo must be non-negative')
        if hi is None: hi = len(a)
        while lo < hi:
            mid = (lo+hi)//2
            if a[mid] > x: lo = mid+1
            else: hi = mid
        return lo
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weight = [self.rev_bisect_left(i, 0) for i in mat]
        return sorted(range(len(weight)), key=lambda i: weight[i])[:k]
# @lc code=end

print(Solution().kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2))