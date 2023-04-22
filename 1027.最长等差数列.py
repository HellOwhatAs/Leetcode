#
# @lc app=leetcode.cn id=1027 lang=python3
#
# [1027] 最长等差数列
#

# @lc code=start
from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        tmp = max(nums) - min(nums)
        cnt, ret = {}, 0
        for d in range(-tmp, tmp + 1):
            cnt.clear()
            for i in nums:
                if i - d in cnt: cnt[i] = cnt[i - d] + 1
                else: cnt[i] = 1
            ret = max(ret, max(cnt.values()))
        return ret
# @lc code=end

print(Solution().longestArithSeqLength(nums = [9,4,7,2,10]))
print(Solution().longestArithSeqLength([20,1,15,3,10,5,8]))