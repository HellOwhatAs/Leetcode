#
# @lc app=leetcode.cn id=1805 lang=python3
#
# [1805] 字符串中不同整数的数目
#

# @lc code=start
import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # return len({int(i) for i in re.sub(r"[a-z]"," ",word).split()})
        return len(set(each.lstrip("0") for each in re.findall(r"([0-9]+)",word)))
# @lc code=end
print(Solution().numDifferentIntegers("a1b01c001"))