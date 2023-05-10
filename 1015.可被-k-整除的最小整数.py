#
# @lc app=leetcode.cn id=1015 lang=python3
#
# [1015] 可被 K 整除的最小整数
#

# @lc code=start
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0: return -1
        ret, val = 1, 1
        for _ in range(k):
            if val % k == 0: return ret
            val = val * 10 + 1
            ret += 1
        return -1
# @lc code=end

