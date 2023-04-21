#
# @lc app=leetcode.cn id=1187 lang=python3
#
# [1187] 使数组严格递增
#

# @lc code=start
from typing import List
from bisect import bisect_left
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        maxv = 1000000000
        arr1 = [-1] + arr1 + [maxv + 5]
        arr2 = sorted(list(set(arr2)))
        n = len(arr1)

        dp = [0] + [maxv]*(n-1)
        for i in range(1,n):
            j = bisect_left(arr2, arr1[i])
            for k in range(1, min(i-1, j) + 1):
                if arr1[i-k-1] < arr2[j-k]:
                    dp[i] = min(dp[i], dp[i-k-1] + k)
            if arr1[i-1] < arr1[i]:
                dp[i] = min(dp[i], dp[i-1])

        return dp[-1] if dp[-1] < maxv else -1
# @lc code=end

