#
# @lc app=leetcode.cn id=1681 lang=python3
#
# [1681] 最小不兼容性
#

# @lc code=start
from typing import List
from math import inf, isinf
from collections import defaultdict
class Solution:
    @staticmethod
    def func(nums: List[int], mask: int):
        Min, Max = inf, -inf
        visited = set()
        for i, elem in enumerate(nums):
            if mask & (1 << i):
                if elem in visited:
                    return None
                visited.add(elem)
                Min, Max = min(Min, elem), max(Max, elem)
        return Max - Min
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = n // k
        dp = defaultdict(lambda:inf)
        for mask in range(1 << n):
            if mask.bit_count() != m: continue
            incomp = self.func(nums, mask)
            if incomp is not None:
                dp[mask] = self.func(nums, mask)
        ori_dp = dp.copy()
        for _k in range(1, k):
            new_dp = defaultdict(lambda:inf)
            for mask in ori_dp:
                for old_mask in dp:
                    if old_mask & mask: continue
                    new_dp[old_mask | mask] = min(new_dp[old_mask | mask], dp[old_mask] + ori_dp[mask])
            dp = new_dp.copy()
        return -1 if isinf(ret := dp[(1<<n) - 1]) else ret
# @lc code=end

print(Solution().minimumIncompatibility(nums = [1,2,1,4], k = 2))
print(Solution().minimumIncompatibility(nums = [6,3,8,1,3,1,2,2], k = 4))
print(Solution().minimumIncompatibility(nums = [5,3,3,6,3,3], k = 3))
print(Solution().minimumIncompatibility(nums = list(range(16)), k = 2))