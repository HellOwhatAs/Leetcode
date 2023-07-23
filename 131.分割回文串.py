#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
from typing import List
class Solution:
    def func(self, mask: int, s: str = None):
        if s is None: s = self.s
        idx = 1
        ret, rret = [0], []
        while mask:
            if mask & 1: ret.append(idx)
            mask >>= 1
            idx += 1
        ret.append(len(s))
        for i in range(1, len(ret)):
            rret.append(s[ret[i-1]:ret[i]])
            if rret[-1] != rret[-1][::-1]: return None
        return rret
        
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        ret = []
        for mask in range(1<<(len(s) - 1)):
            tmp = self.func(mask)
            if tmp is not None:
                ret.append(tmp)
        return ret

# @lc code=end
print(Solution().partition("0123456789"))
print(Solution().partition("aab"))
print(Solution().partition("a"))
print(Solution().partition("a" * 16))
