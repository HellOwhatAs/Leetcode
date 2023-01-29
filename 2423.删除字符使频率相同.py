#
# @lc app=leetcode.cn id=2423 lang=python3
#
# [2423] 删除字符使频率相同
#

# @lc code=start
from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        return min((c:=Counter(word)).values()) == 1 and ((lencvC:=len(Counter(c.values()))) == 2 and list(c.values()).count(1) <= 1 or lencvC == 1) or (maxcv:=max(c.values())) - (mincv:=min(c.values())) == 1 and sum(c.values()) == maxcv + mincv * (len(c) - 1) or len(c) == 1
# @lc code=end

print(Solution().equalFrequency("zz"))