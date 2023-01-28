#
# @lc app=leetcode.cn id=1774 lang=python3
#
# [1774] 最接近目标价格的甜点成本
#

# @lc code=start
from typing import List
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        x = min(baseCosts)
        if x > target:return x
        can = [False] * (target + 1)
        ans = 2 * target - x
        for c in baseCosts:
            if c <= target:can[c] = True
            else:ans = min(ans, c)
        toppingCosts_=[]
        for _ in toppingCosts:(toppingCosts_.append(_),toppingCosts_.append(_))
        toppingCosts_, toppingCosts = toppingCosts, toppingCosts_
        for c in toppingCosts:
            for i in range(target, 0, -1):
                if can[i] and i + c > target:ans = min(ans, i + c)
                if i > c: can[i] |= can[i - c]
                # print("|"+"|".join(str(ind).rjust(2) if _ else "  " for ind,_ in enumerate(can))+"|", 
                # "toppingCost = {}".format(c).ljust(20), "i = {}".format(i))
        for i in range(ans - target + 1):
            if can[target - i]:return target - i
        return ans
# @lc code=end
assert Solution().closestCost([2,3], [4,5,100], 18) == 17