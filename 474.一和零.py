#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
from typing import List
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def func(self, start: int, m: int, n: int) -> int:
        if start == len(self.nums): return 0
        c1, c0 = self.nums[start]
        ret = self.func(start + 1, m, n)
        if c0 <= m and c1 <= n:
            ret = max(ret, self.func(start + 1, m - c0, n - c1) + 1)
        return ret

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.nums = [(tmp := i.count('1'), len(i) - tmp) for i in strs]
        return self.func(0, m, n)
# @lc code=end

print(Solution().findMaxForm(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3))
print(Solution().findMaxForm(strs = ["10", "0", "1"], m = 1, n = 1))
print(Solution().findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], 9, 80))