#
# @lc app=leetcode.cn id=1984 lang=python3
#
# [1984] 学生分数的最小差值
#

# @lc code=start
from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ret = nums[-1]
        for i in range(k - 1, len(nums)):
            ret = min(ret, nums[i] - nums[i - k + 1])
        return ret
# @lc code=end

print(Solution().minimumDifference([90], k = 1))