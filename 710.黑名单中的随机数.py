#
# @lc app=leetcode.cn id=710 lang=python3
#
# [710] 黑名单中的随机数
#

# @lc code=start
from typing import List
import random
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.b=blacklist
        self.n=n
        self.iter=iter(self.func())
    def func(self):
        while True:
            for i in range(self.n):
                if i in self.b:
                    continue
                yield i
    def pick(self) -> int:
        return next(self.iter)
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end

