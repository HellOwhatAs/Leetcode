#
# @lc app=leetcode.cn id=1605 lang=python3
#
# [1605] 给定行和列的和求可行矩阵
#

# @lc code=start
from typing import List
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        ret = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ret[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= ret[i][j]
                colSum[j] -= ret[i][j]
        return ret
# @lc code=end

print(Solution().restoreMatrix(rowSum = [3,8], colSum = [4,7]))