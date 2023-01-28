#
# @lc app=leetcode.cn id=1235 lang=python3
#
# [1235] 规划兼职工作
#

# @lc code=start
from typing import List,Callable
def last_false(lb:int,ub:int,func:Callable[[int],bool],not_find=None)->int:
    while lb+1<ub:
        mid=(lb+ub)//2
        if func(mid):ub=mid
        else:lb=mid
    if not func(ub):return ub
    if not func(lb):return lb
    return not_find
def first_true(lb:int,ub:int,func:Callable[[int],bool],not_find=None)->int:
    while lb+1<ub:
        mid=(lb+ub)//2
        if func(mid):ub=mid
        else:lb=mid
    if func(lb):return lb
    if func(ub):return ub
    return not_find
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        order=sorted(list(range(len(startTime))),key=lambda i:endTime[i])
        dp=[0]*(len(order))
        for i in range(len(order)):
            k=first_true(0,len(order)-1,lambda k:endTime[order[k]]>startTime[order[i]],-1)
            dp[i]=max(dp[i-1],dp[k-1]+profit[order[i]])
        return dp[-1]
# @lc code=end

print(Solution().jobScheduling(
    [1,2,3,4,6],
    [3,5,10,6,9],
    [20,20,100,70,60]
))