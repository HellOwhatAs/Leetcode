#
# @lc app=leetcode.cn id=777 lang=python3
#
# [777] 在LR字符串中交换相邻字符
#

# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        s=[(i,ind) for ind,i in enumerate(start) if i!='X']
        e=[(i,ind) for ind,i in enumerate(end)   if i!='X']
        if len(s)!=len(e):return False
        for i,j in zip(s,e):
            if i[0]!=j[0] or i[0]=='L' and i[1]<j[1] or i[0]=='R' and i[1]>j[1]:return False
        return True
# @lc code=end
print(Solution().canTransform("X","L"))
