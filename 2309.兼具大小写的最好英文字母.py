#
# @lc app=leetcode.cn id=2309 lang=python3
#
# [2309] 兼具大小写的最好英文字母
#

# @lc code=start
from collections import Counter
class Solution:
    def greatestLetter(self, s: str) -> str:
        c = Counter(s)
        tmp = [chr(i) for i in range(ord("A"), ord("Z") + 1) if chr(i) in c and chr(i).lower() in c]
        return max(tmp) if tmp else ''
# @lc code=end

print(Solution().greatestLetter("AbCdEfGhIjK"))