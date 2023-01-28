#
# @lc app=leetcode.cn id=2535 lang=python3
#
# [2535] 数组元素和与数字和的绝对差
#

# @lc code=start
from typing import List
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ret = 0
        for i in nums:
            ret += i
            while i:
                ret -= i % 10
                i //= 10
        return ret
# @lc code=end

print(Solution().differenceOfSum([1,2,3,4]))