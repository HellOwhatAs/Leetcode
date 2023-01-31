#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换水问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ret = numBottles
        while numBottles >= numExchange:
            ret += (tmp := numBottles // numExchange)
            numBottles = tmp + numBottles % numExchange
        return ret
# @lc code=end

print(Solution().numWaterBottles(numBottles = 15, numExchange = 4))