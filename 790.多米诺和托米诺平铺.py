#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#

# @lc code=start
import numpy as np
class Solution:
    mod=np.int64(1000000007)
    @staticmethod
    def matrixPow(mat: np.ndarray, n: int) -> np.ndarray:
        ret=np.eye(4,dtype=np.int64)
        while n:
            if n&1:ret=ret@mat%Solution.mod
            n>>=1
            mat=mat@mat%Solution.mod
        return ret
    def numTilings(self, n: int) -> int:
        dp=np.array([0,0,0,1],dtype=np.int64)
        X=np.array([
            [0,1,1,1],
            [0,0,1,1],
            [0,1,0,1],
            [1,0,0,1]
        ],dtype=np.int64)
        dp=dp@self.matrixPow(X,n)
        return int(dp[3])
# @lc code=end

print(Solution().numTilings(3000000))