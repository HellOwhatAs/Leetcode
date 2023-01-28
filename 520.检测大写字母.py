#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or not (word1:=word[1:]) or word1.islower()
# @lc code=end

