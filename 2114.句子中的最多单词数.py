#
# @lc app=leetcode.cn id=2114 lang=python3
#
# [2114] 句子中的最多单词数
#

# @lc code=start
from typing import List
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(i.split()) for i in sentences)
# @lc code=end

for i in [
    ["alice and bob love leetcode", "i think so too", "this is great thanks very much"],
    ["please wait", "continue to fight", "continue to win"]
]:
    print(Solution().mostWordsFound(i))