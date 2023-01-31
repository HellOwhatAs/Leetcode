#
# @lc app=leetcode.cn id=1437 lang=python3
#
# [1437] 是否所有 1 都至少相隔 k 个元素
#

# @lc code=start
from typing import List
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        tmp = [ii for ii, i in enumerate(nums) if i]
        for i in range(1, len(tmp)):
            if tmp[i] - tmp[i - 1] <= k:
                return False
        return True
# @lc code=end

print(Solution().kLengthApart(nums = [0,1,0,1], k = 1))