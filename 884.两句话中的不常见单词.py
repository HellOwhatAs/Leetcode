#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [k for k, v in Counter((*s1.split(), *s2.split())).items() if v == 1]
# @lc code=end

print(Solution().uncommonFromSentences( "apple apple", s2 = "banana"))