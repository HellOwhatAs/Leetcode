#
# @lc app=leetcode.cn id=1753 lang=python3
#
# [1753] 移除石子的最大得分
#

# @lc code=start
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a,b,c=sorted([a,b,c])
        return a+b if a+b<=c else (a+b+c)//2
# @lc code=end

