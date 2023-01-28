#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

# @lc code=start
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dp_single=[0]*len(fruits)
        dp_double=[None]*len(fruits)
        for i in range(0,len(fruits)):
            if fruits[i]!=fruits[0]:
                dp_double[i]=(i+1,fruits[0])
                dp_single[i]=1
                break
            else:dp_double[i]=(0,)
        else:return len(fruits)
        for j in range(i+1,len(fruits)):
            if fruits[j]==fruits[j-1]:
                dp_single[j]=dp_single[j-1]+1
                dp_double[j]=dp_double[j-1][0]+1,dp_double[j-1][1]
            elif fruits[j]==dp_double[j-1][1]:
                dp_single[j]=1
                dp_double[j]=dp_double[j-1][0]+1,fruits[j-1]
            else:
                dp_single[j]=1
                dp_double[j]=dp_single[j-1]+1,fruits[j-1]
        return max(max(dp_single),max(i[0] for i in dp_double))
# @lc code=end

print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))