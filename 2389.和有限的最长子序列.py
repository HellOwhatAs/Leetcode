#
# @lc app=leetcode.cn id=2389 lang=python3
#
# [2389] 和有限的最长子序列
#

# @lc code=start
from typing import List
import bisect
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)): nums[i] += nums[i - 1]
        return [bisect.bisect_right(nums, i) for i in queries]
# @lc code=end

print(Solution().answerQueries(nums = [2,3,4,5], queries = [1]))