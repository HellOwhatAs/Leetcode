#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import List
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [j for i in range(len(nums)+1) for j in combinations(nums,i)]
# @lc code=end

print(Solution().subsets([1,2,3]))