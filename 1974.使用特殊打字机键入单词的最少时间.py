#
# @lc app=leetcode.cn id=1974 lang=python3
#
# [1974] 使用特殊打字机键入单词的最少时间
#

# @lc code=start
class Solution:
    @staticmethod
    def CharDistance(a: str, b: str) -> int:
        orda, ordb = ord(a), ord(b)
        if orda > ordb: orda, ordb = ordb, orda
        return min(ordb - orda, orda + 26 - ordb)
    def minTimeToType(self, word: str) -> int:
        return len(word) + sum(self.CharDistance(word[i - 1] if i > 0 else 'a', word[i]) for i in range(len(word)))
# @lc code=end

print(Solution().minTimeToType("abc"))
print(Solution().minTimeToType("bza"))
print(Solution().minTimeToType("zjpc"))