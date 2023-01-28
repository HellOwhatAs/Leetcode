#
# @lc app=leetcode.cn id=1859 lang=python3
#
# [1859] 将句子排序
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join(i[:-1] for i in sorted(s.split(), key=lambda x:x[-1]))
# @lc code=end

print(Solution().sortSentence(s = "Myself2 Me1 I4 and3"))