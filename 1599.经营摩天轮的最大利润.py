#
# @lc app=leetcode.cn id=1599 lang=python3
#
# [1599] 经营摩天轮的最大利润
#

# @lc code=start
from typing import List
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        count, waiting, profit = 0, customers[0], 0
        ret, max_profit = 0, float('-inf')
        while waiting or count < len(customers):
            boarding = min(4, waiting)
            profit += boarding * boardingCost - runningCost
            waiting -= boarding
            count += 1
            if count < len(customers):
                waiting += customers[count]
            if profit > max_profit:
                max_profit = profit
                ret = count
        return ret if max_profit > 0 else -1
# @lc code=end

print(Solution().minOperationsMaxProfit(customers = [8,3], boardingCost = 5, runningCost = 6))
print(Solution().minOperationsMaxProfit(customers = [10,9,6], boardingCost = 6, runningCost = 4))
print(Solution().minOperationsMaxProfit(customers = [3,4,0,5,1], boardingCost = 1, runningCost = 92))