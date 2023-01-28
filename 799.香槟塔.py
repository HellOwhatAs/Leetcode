#
# @lc app=leetcode.cn id=799 lang=python3
#
# [799] 香槟塔
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        d=[[0.0]*(i+1) for i in range(query_row+1)]
        d[0][0]=poured
        for i in range(query_row):
            for j in range(i+1):
                if d[i][j]>1.:
                    tmp,d[i][j]=(d[i][j]-1.0)/2,1.0
                    d[i+1][j]+=tmp
                    d[i+1][j+1]+=tmp
        return min(d[query_row][query_glass],1.0)
# @lc code=end

print(Solution().champagneTower(100000009,33,17))