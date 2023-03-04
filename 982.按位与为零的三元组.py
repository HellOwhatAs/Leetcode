#
# @lc app=leetcode.cn id=982 lang=python3
#
# [982] 按位与为零的三元组
#

# @lc code=start
from typing import List
from collections import Counter
from itertools import product
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        return sum(v0 for (k0, v0), k in product(Counter(nums[i] & nums[j] for i, j in product(range(len(nums)), range(len(nums)))).items(), range(len(nums))) if k0 & nums[k] == 0)
# @lc code=end

print(Solution().countTriplets(nums = [2,1,3]))
print(Solution().countTriplets(nums = [0,0,0]))