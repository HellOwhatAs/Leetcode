#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
from typing import List
from math import inf
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff, ret = inf, None
        nums.sort()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            t = target - nums[i]
            while j < k:
                if nums[j] + nums[k] == t: return target
                else:
                    d = abs(nums[j] + nums[k] - t)
                    if d < diff: diff, ret = d, nums[j] + nums[k] + nums[i]
                if nums[j] + nums[k] > t: k -= 1
                else: j += 1
        return ret
                
# @lc code=end

print(Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(Solution().threeSumClosest(nums = [0,0,0], target = 1))