#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        ret=[]
        stack=[]
        for i in s:
            if i in "aeiouAEIOU":
                ret.append(None)
                stack.append(i)
            else:ret.append(i)
        for i in range(len(ret)):
            if ret[i]==None:
                ret[i]=stack.pop()
        return "".join(ret)
# @lc code=end

