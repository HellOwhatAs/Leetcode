#
# @lc app=leetcode.cn id=2490 lang=python3
#
# [2490] 回环句
#

# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        return [words:=sentence.split(), all(words[i][0] == words[i - 1][-1] for i in range(len(words)))][1]
# @lc code=end

print(Solution().isCircularSentence("Leetcode is cool"))