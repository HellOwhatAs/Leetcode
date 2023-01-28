#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
from typing import List
import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned, paragraph = set(banned), Counter(re.sub(r"(\!|\?|\'|\,|\;|\.)", ' ', paragraph.lower()).split())
        return max(paragraph.keys(), key=lambda x:0 if x in banned else paragraph[x])
# @lc code=end

print(Solution().mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))