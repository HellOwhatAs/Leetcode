#
# @lc app=leetcode.cn id=1590 lang=python3
#
# [1590] 使数组和能被 P 整除
#

# @lc code=start
from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        t = sum(nums) % p
        if t == 0: return 0
        index, prefix_sum, ret = {0: -1}, 0, len(nums)
        for idx, elem in enumerate(nums):
            prefix_sum = (prefix_sum + elem) % p
            tmp = (prefix_sum - t) % p
            if tmp in index:
                ret = min(ret, idx - index[tmp])
            index[prefix_sum] = idx
        return ret if ret < len(nums) else -1
# @lc code=end

print(Solution().minSubarray(nums = [3,1,4,2], p = 6))
print(Solution().minSubarray(nums = [6,3,5,2], p = 9))
print(Solution().minSubarray(nums = [1,2,3], p = 3))
print(Solution().minSubarray(nums = [1,2,3], p = 7))
print(Solution().minSubarray([1000000000,1000000000,1000000000], p = 3))
print(Solution().minSubarray([8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2], 148))