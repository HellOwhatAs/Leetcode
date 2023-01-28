#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret=[]
        while columnNumber:
            if columnNumber%26==0:
                ret.append('Z')
                columnNumber=(columnNumber)//26-1
            else:
                ret.append(chr(ord('A')+(columnNumber)%26-1))
                columnNumber=(columnNumber)//26
        return "".join(reversed(ret))
# @lc code=end

print(Solution().convertToTitle(701))