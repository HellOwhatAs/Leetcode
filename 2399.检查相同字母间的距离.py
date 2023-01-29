#
# @lc app=leetcode.cn id=2399 lang=python3
#
# [2399] 检查相同字母间的距离
#

# @lc code=start
from typing import List
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        idx = {}
        for i, c in enumerate(s):
            if c in idx:
                if i - idx[c] - 1 != distance[ord(c) - ord('a')]:
                    return False
            else: idx[c] = i
        return True
        
# @lc code=end

print(Solution().checkDistances(s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))