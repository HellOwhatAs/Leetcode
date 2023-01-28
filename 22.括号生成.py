#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List
from functools import lru_cache
class Solution:
    @lru_cache
    def generateParenthesis(self, n: int) -> List[str]:
        return [""] if n==0 else list(set("{}({}){}".format(s1,s2,s3) for i in range(n) for j in range(i,n) for s1 in self.generateParenthesis(i) for s2 in self.generateParenthesis(j-i) for s3 in self.generateParenthesis(n-1-j)))
# @lc code=end

