#
# @lc app=leetcode.cn id=1144 lang=python3
#
# [1144] 递减元素使数组呈锯齿状
#

# @lc code=start
from typing import List
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        return min(
            sum(
                max(
                    max(0, nums[i] - nums[i - 1] + 1) if i - 1 >= 0 else 0,
                    max(0, nums[i] - nums[i + 1] + 1) if i + 1 < len(nums) else 0
                )
                for i in range(0, len(nums), 2)
            ),
            sum(
                max(
                    max(0, nums[i] - nums[i - 1] + 1) if i - 1 >= 0 else 0,
                    max(0, nums[i] - nums[i + 1] + 1) if i + 1 < len(nums) else 0
                )
                for i in range(1, len(nums), 2)
            )
        )
# @lc code=end

print(Solution().movesToMakeZigzag(nums = [1,2,3]))
print(Solution().movesToMakeZigzag(nums = [9,6,1,6,2]))
print(Solution().movesToMakeZigzag(nums = [2,1,2]))