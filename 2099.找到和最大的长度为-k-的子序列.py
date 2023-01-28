#
# @lc app=leetcode.cn id=2099 lang=python3
#
# [2099] 找到和最大的长度为 K 的子序列
#

# @lc code=start
from typing import List
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return [nums[i] for i in sorted(sorted(list(range(len(nums))), key=lambda i:nums[i])[-k:])]
# @lc code=end

print(Solution().maxSubsequence([3,4,3,3], k = 2))