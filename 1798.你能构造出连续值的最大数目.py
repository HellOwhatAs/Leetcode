#
# @lc app=leetcode.cn id=1798 lang=python3
#
# [1798] 你能构造出连续值的最大数目
#

# @lc code=start
from typing import List
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        ret = 0
        for i in coins:
            if i <= ret + 1: ret += i
            else: break
        return ret + 1
# @lc code=end

print(Solution().getMaximumConsecutive([1,4,10,3,1]))