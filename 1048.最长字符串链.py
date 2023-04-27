#
# @lc app=leetcode.cn id=1048 lang=python3
#
# [1048] 最长字符串链
#

# @lc code=start
from typing import List
class Solution:
    @staticmethod
    def func(a: str, b: str) -> bool:
        if len(a) + 1 != len(b): return False
        i, j = 0, 0
        while i < len(a) and j < len(b): i, j = i + (a[i] == b[j]), j + 1
        return i == len(a) and (j == len(b) or i == j)
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = [1] * len(words)
        for i in range(1, len(words)):
            for j in range(i):
                if self.func(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# @lc code=end

print(Solution().longestStrChain(words = ["a","b","ba","bca","bda","bdca"]))
print(Solution().longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]))
print(Solution().longestStrChain(words = ["abcd","dbqca"]))