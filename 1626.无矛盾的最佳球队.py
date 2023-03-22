#
# @lc app=leetcode.cn id=1626 lang=python3
#
# [1626] 无矛盾的最佳球队
#

# @lc code=start
from typing import List
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scores.append(0), ages.append(0)
        self.data = sorted(zip(scores, ages), key=lambda x:(x[1], x[0]))
        n = len(self.data)
        dp = [[0] * n for _ in range(n + 1)]
        for idx in reversed(range(n)):
            for val in range(idx):
                if self.data[idx][1] > self.data[val][1] and self.data[idx][0] < self.data[val][0]:
                    dp[idx][val] = dp[idx + 1][val]
                else:
                    dp[idx][val] = max(
                        dp[idx + 1][val],
                        dp[idx + 1][idx] + self.data[idx][0]
                    )
        return dp[1][0]

# @lc code=end

print(Solution().bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))
print(Solution().bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1]))
print(Solution().bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1]))