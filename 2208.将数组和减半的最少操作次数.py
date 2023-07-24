#
# @lc app=leetcode.cn id=2208 lang=python3
#
# [2208] 将数组和减半的最少操作次数
#

# @lc code=start
from typing import List
import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        ret = 0
        for i in range(len(nums)): nums[i] *= -1
        heapq.heapify(nums)
        while target > 0:
            tmp = heapq.heappop(nums) / 2
            heapq.heappush(nums, tmp)
            target += tmp
            ret += 1
        return ret
# @lc code=end

print(Solution().halveArray(nums = [5,19,8,1]))
print(Solution().halveArray(nums = [3,8,20]))