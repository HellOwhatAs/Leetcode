#
# @lc app=leetcode.cn id=2085 lang=python3
#
# [2085] 统计出现过一次的公共字符串
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        return len({k for k,v in Counter(words1).items() if v == 1} & {k for k,v in Counter(words2).items() if v == 1})
# @lc code=end

print(Solution().countWords(words1 = ["a","ab"], words2 = ["a","a","a","ab"]))