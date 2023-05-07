#
# @lc app=leetcode.cn id=1010 lang=python3
#
# [1010] 总持续时间可被 60 整除的歌曲
#

# @lc code=start
from typing import List
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem = [0] * 60
        for i in time: rem[i % 60] += 1
        return (rem[0] * (rem[0] - 1) + rem[30] * (rem[30] - 1)) // 2 + sum(rem[i] * rem[60 - i] for i in range(1, 30))
# @lc code=end

print(Solution().numPairsDivisibleBy60(time = [30,20,150,100,40]))
print(Solution().numPairsDivisibleBy60(time = [60,60,60]))