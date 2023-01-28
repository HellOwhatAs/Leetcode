#
# @lc app=leetcode.cn id=1935 lang=python3
#
# [1935] 可以输入的最大单词数
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters_set, ret = set(brokenLetters), 0
        for word in text.split():
            for char in word:
                if char in brokenLetters_set:
                    break
            else: ret += 1
        return ret
# @lc code=end

print(Solution().canBeTypedWords(text = "leet code", brokenLetters = "e"))