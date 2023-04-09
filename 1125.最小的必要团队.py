#
# @lc app=leetcode.cn id=1125 lang=python3
#
# [1125] 最小的必要团队
#

# @lc code=start
from typing import List
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m = len(req_skills), len(people)
        skill_index = {v: i for i, v in enumerate(req_skills)}
        dp = [None] * (1 << n)
        dp[0] = []
        for i, p in enumerate(people):
            cur_skill = 0
            for s in p:
                cur_skill |= 1 << skill_index[s]
            for prev in range(1 << n):
                if dp[prev] == None:
                    continue
                comb = prev | cur_skill
                if dp[comb] == None or len(dp[comb]) > len(dp[prev]) + 1:
                    dp[comb] = dp[prev] + [i]
        return dp[(1 << n) - 1]
# @lc code=end

