#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

# @lc code=start
from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        i=iter(permutations(range(n),n))
        for _ in range(k-1):next(i)
        return "".join(str(j+1) for j in next(i))
# @lc code=end