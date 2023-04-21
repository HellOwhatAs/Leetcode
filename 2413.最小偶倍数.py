#
# @lc app=leetcode.cn id=2413 lang=python3
#
# [2413] 最小偶倍数
#

# @lc code=start
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * (n % 2 + 1)
# @lc code=end

print(Solution().smallestEvenMultiple(n = 5))
print(Solution().smallestEvenMultiple(n = 6))