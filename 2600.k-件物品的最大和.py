#
# @lc app=leetcode.cn id=2600 lang=python3
#
# [2600] K 件物品的最大和
#

# @lc code=start
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ret = 0
        if k > numOnes:
            ret += numOnes
            k -= numOnes
        else: return k
        
        if k > numZeros:
            k -= numZeros
        else: return ret

        return ret - k
# @lc code=end

print(Solution().kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2))
print(Solution().kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4))