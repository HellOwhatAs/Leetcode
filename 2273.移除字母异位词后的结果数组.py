#
# @lc app=leetcode.cn id=2273 lang=python3
#
# [2273] 移除字母异位词后的结果数组
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ret, RetBackCounter = [], None
        for word in words:
            if RetBackCounter != (tmp:=Counter(word)) or RetBackCounter is None:
                RetBackCounter = tmp
                ret.append(word)
        return ret
# @lc code=end

print(Solution().removeAnagrams(["a","b","c","d","e"]))