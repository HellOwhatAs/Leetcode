#
# @lc app=leetcode.cn id=2357 lang=python3
#
# [2357] 使数组中所有元素都等于零
#

# @lc code=start
from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(i for i in nums if i > 0))
# @lc code=end

print(Solution().minimumOperations([0]))