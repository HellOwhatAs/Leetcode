#
# @lc app=leetcode.cn id=1238 lang=python3
#
# [1238] 循环码排列
#

# @lc code=start
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [0,1] if n == 1 else (tmp := self.grayCode(n - 1)) + [i | (1 << (n - 1)) for i in reversed(tmp)]
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [i ^ start for i in self.grayCode(n)]
# @lc code=end

print(Solution().circularPermutation(n = 3, start = 2))