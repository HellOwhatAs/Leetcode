#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for ii, i in enumerate(prices):
            while stack and prices[stack[-1]] >= i:
                prices[stack.pop()] -= i
            stack.append(ii)
        return prices
# @lc code=end

print(Solution().finalPrices([8,4,6,2,3]))