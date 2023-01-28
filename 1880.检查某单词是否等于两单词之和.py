#
# @lc app=leetcode.cn id=1880 lang=python3
#
# [1880] 检查某单词是否等于两单词之和
#

# @lc code=start
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return int("".join(str(ord(i) - ord('a')) for i in firstWord)) + int("".join(str(ord(i) - ord('a')) for i in secondWord)) == int("".join(str(ord(i) - ord('a')) for i in targetWord))
# @lc code=end

print(Solution().isSumEqual("aaa", secondWord = "a", targetWord = "aaaa"))