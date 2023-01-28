#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ret=0
        for i in range(len(columnTitle)):
            ret*=26
            ret+=ord(columnTitle[i])-ord('A')+1
        return ret
# @lc code=end

print(Solution().titleToNumber("AA"))