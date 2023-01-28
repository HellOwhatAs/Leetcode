#
# @lc app=leetcode.cn id=2006 lang=python3
#
# [2006] 差的绝对值为 K 的数对数目
#

# @lc code=start
from typing import List
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ret, n = 0, len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if abs(nums[i] - nums[j]) == k:
                    ret += 1
        return ret
# @lc code=end

print(Solution().countKDifference(nums = [3,2,1,5,4], k = 2))