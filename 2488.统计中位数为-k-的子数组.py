#
# @lc app=leetcode.cn id=2488 lang=python3
#
# [2488] 统计中位数为 K 的子数组
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        kidx = nums.index(k)
        data = defaultdict(int)
        data[0] = 1
        sum, ret = 0, 0
        sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)
        for i, elem in enumerate(nums):
            sum += sign(elem - k)
            if i < kidx: data[sum] += 1
            else: ret += data[sum] + data[sum - 1]
        return ret
# @lc code=end

print(Solution().countSubarrays(nums = [3,2,1,4,5], k = 4))
print(Solution().countSubarrays(nums = [2,3,1], k = 3))