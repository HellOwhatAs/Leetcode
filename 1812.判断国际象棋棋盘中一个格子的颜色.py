#
# @lc app=leetcode.cn id=1812 lang=python3
#
# [1812] 判断国际象棋棋盘中一个格子的颜色
#

# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a=(ord(coordinates[0])-ord('a'))%2==0
        b=(int(coordinates[1])-1)%2==0
        return a!=b
# @lc code=end

print(Solution().squareIsWhite('c7'))