#
# @lc app=leetcode.cn id=1995 lang=python3
#
# [1995] 统计特殊四元组
#

# @lc code=start
from typing import List
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n, ret = len(nums), 0
        for a in range(n-3):
            for b in range(a+1, n-2):
                for c in range(b+1, n-1):
                    for d in range(c+1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            ret += 1
        return ret
# @lc code=end

print(Solution().countQuadruplets([1,1,1,3,5]))