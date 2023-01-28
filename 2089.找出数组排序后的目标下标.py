#
# @lc app=leetcode.cn id=2089 lang=python3
#
# [2089] 找出数组排序后的目标下标
#

# @lc code=start
from typing import List
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ret, start = [], 0
        while True:
            try:
                idx = nums.index(target, start)
                start = idx + 1
                ret.append(idx)
            except:
                return ret
# @lc code=end

print(Solution().targetIndices(nums = [1,2,5,2,3], target = 4))