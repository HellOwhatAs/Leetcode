#
# @lc app=leetcode.cn id=1186 lang=python3
#
# [1186] 删除一次得到子数组最大和
#

# @lc code=start
from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp = [-float('inf')] * len(arr)
        dp2 = [-float('inf')] * len(arr)
        dp[0] = dp2[0] = arr[0]
        for i in range(1, len(arr)):
            if dp[i - 1] <= 0:
                dp[i] = arr[i]
            else:
                dp[i] = dp[i - 1] + arr[i]

            dp2[i] = max(dp[i - 1], dp2[i - 1] + arr[i])

        return max(*dp, *dp2)
# @lc code=end

print(Solution().maximumSum(arr = [1,-2,0,3]))
print(Solution().maximumSum(arr = [1,-2,-2,3]))
print(Solution().maximumSum(arr = [-1,-1,-1,-1]))
print(Solution().maximumSum([2,1,-2,-5,-2]))