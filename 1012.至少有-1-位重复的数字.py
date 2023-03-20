#
# @lc app=leetcode.cn id=1012 lang=python3
#
# [1012] 至少有 1 位重复的数字
#

# @lc code=start
from functools import lru_cache
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        A = list(map(int, str(n)))
        N = len(A)
        @lru_cache(None)
        def f(i, tight, mask, hasDup):
            if i >= N:
                if hasDup:
                    return 1
                return 0
            upperLimit = A[i] if tight else 9
            ans = 0
            for d in range(upperLimit + 1):
                tight2 = tight and d == upperLimit
                mask2 = mask if mask == 0 and d == 0 else mask | (1 << d)
                hasDup2 = hasDup or (mask & (1 << d))
                ans += f(i + 1, tight2, mask2, hasDup2)
            return ans
        return f(0, True, 0, False)
        
# @lc code=end

print(Solution().numDupDigitsAtMostN(10000000))