#
# @lc app=leetcode.cn id=1043 lang=python3
#
# [1043] 分隔数组以得到最大和
#

# @lc code=start
from typing import List
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp: List[int] = [0] * len(arr)
        for i in range(1, k + 1):
            dp[i - 1] = max(arr[:i]) * i
        for i in range(k, len(arr)):
            for j in range(1, k + 1):
                dp[i] = max(dp[i], dp[i - j] + max(arr[i - j + 1: i + 1]) * j)
        return dp[-1]
# @lc code=end

print(Solution().maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3))
print(Solution().maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4))