#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#

# @lc code=start
from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        dp_max, dp_min = [(nums[0], 1)], [(nums[0], 1)]
        for i in range(1, len(nums)):
            dp_max.append(max((dp_max[-1][0] + nums[i], dp_max[-1][1] + 1), (nums[i], 1)))
            dp_min.append(min((dp_min[-1][0] + nums[i], dp_min[-1][1] + 1), (nums[i], 1)))
        ret = max(dp_max)[0]
        min_val, min_l = min(dp_min)
        if min_l < len(nums): ret = max(ret, sum(nums) - min_val)
        return ret
# @lc code=end

print(Solution().maxSubarraySumCircular(nums = [1,-2,3,-2]))
print(Solution().maxSubarraySumCircular(nums = [5,-3,5]))
print(Solution().maxSubarraySumCircular(nums = [3,-2,2,-3]))
print(Solution().maxSubarraySumCircular([-2]))