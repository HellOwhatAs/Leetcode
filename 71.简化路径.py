#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path=[i for i in path.split('/') if i and i!='.']
        ret=[]
        for i in path:
            if i!='..':ret.append(i)
            elif ret:ret.pop()
        return "/"+"/".join(ret)
# @lc code=end

print(Solution().simplifyPath("/a/./b/../../c/"))