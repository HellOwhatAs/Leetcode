#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(i[::-1] for i in s.split())
# @lc code=end

print(Solution().reverseWords("东京 爱情 故事"))