#
# @lc app=leetcode.cn id=1759 lang=python3
#
# [1759] 统计同构子字符串的数目
#

# @lc code=start
from itertools import groupby
class Solution:
    def countHomogenous(self, s: str) -> int:
        ret=0
        MOD=10**9+7
        for _,j in groupby(s):
            tmp=len(list(j))
            ret+=(tmp+1)*tmp//2
            ret%=MOD
        return ret
# @lc code=end

print(Solution().countHomogenous("abbcccaa"))