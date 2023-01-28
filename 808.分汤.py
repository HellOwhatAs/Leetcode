#
# @lc app=leetcode.cn id=808 lang=python3
#
# [808] 分汤
#

# @lc code=start
class Solution:
    def soupServings(self, n: int) -> float:
        if n>=5000:return 1.
        n=n//25+bool(n%25)
        dp=[[0.]*(n+1) for _ in range(n+1)]
        dp[0]=[0.5]+[1.0]*n
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j]=(
                    dp[max(0,i-4)][max(0,j  )]+
                    dp[max(0,i-3)][max(0,j-1)]+
                    dp[max(0,i-2)][max(0,j-2)]+
                    dp[max(0,i-1)][max(0,j-3)]
                )/4
        return dp[n][n]

# @lc code=end

print(Solution().soupServings(60))
