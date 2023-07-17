#
# @lc app=leetcode.cn id=2597 lang=python3
#
# [2597] 美丽子集的数目
#

# @lc code=start
from typing import List
class Solution:

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        self.nums = nums
        self.n = n = len(nums)
        self.k = k

        faults = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[j] - nums[i] == k:
                    faults.append(((1 << i), (1 << j)))

        ret = 0
        for mask in range(1, 1<<n):
            if any((mask & i) and (mask & j) for i, j in faults): continue
            ret += 1
        
        return ret
# @lc code=end
print(Solution().beautifulSubsets(nums = [2,4,6], k = 2))
print(Solution().beautifulSubsets(nums = [1], k = 1))
print(Solution().beautifulSubsets([2,2,2,4,4,6,6,6], 2))
print(Solution().beautifulSubsets([10,4,5,7,2,1], 3))