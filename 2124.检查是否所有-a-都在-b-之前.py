#
# @lc app=leetcode.cn id=2124 lang=python3
#
# [2124] 检查是否所有 A 都在 B 之前
#

# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
        return a < b if (a:=s.rfind('a')) != -1 and (b:=s.find('b')) != -1 else True
# @lc code=end

for i in ["aaabbb", "abab", "bbb", "a"]:
    print(Solution().checkString(i))