#
# @lc app=leetcode.cn id=1663 lang=python3
#
# [1663] 具有给定数值的最小字符串
#

# @lc code=start
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        return "".join(('a',(k:=k-1))[0] if (tmp:=(n - i - 1) * 26) >= k - 1 else (chr(k - tmp + ord('a') - 1), (k:=tmp))[0] for i in range(n))

# @lc code=end

print(Solution().getSmallestString(n = 10000, k = 220000))