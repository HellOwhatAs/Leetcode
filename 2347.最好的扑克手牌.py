#
# @lc app=leetcode.cn id=2347 lang=python3
#
# [2347] 最好的扑克手牌
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1: return "Flush"
        tmp = max(Counter(ranks).values())
        if tmp >= 3: return "Three of a Kind"
        if tmp == 2: return "Pair"
        return "High Card"
# @lc code=end

print(Solution().bestHand(ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]))