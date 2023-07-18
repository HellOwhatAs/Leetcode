#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()
        for i in range(1<<len(nums)):
            tmp = i
            idx = 0
            ttmp = []
            while tmp:
                if tmp & 1: ttmp.append(nums[idx])
                idx += 1
                tmp >>= 1
            ret.add(tuple(ttmp))
        return [list(i) for i in ret]
# @lc code=end

print(Solution().subsetsWithDup(nums = [1,2,2]))