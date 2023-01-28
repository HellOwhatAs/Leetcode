#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isInteger(self,s:str)->bool:
        if not s:return False
        if s[0] in "+-":s=s[1:]
        return s.isdecimal()
    def isFloat(self,s:str)->bool:
        if not s:return False
        if s[0] in "+-":s=s[1:]
        ss=s.split('.')
        if(len(ss)!=2):return False
        if (not ss[0]) and (not ss[1]):return False
        return ((not ss[0]) or ss[0].isdecimal()) and ((not ss[1]) or ss[1].isdecimal())
    def isNumber(self, s: str) -> bool:
        s=s.lower()
        ss=s.split('e')
        if len(ss)>2:return False
        if len(ss)==1:return self.isFloat(ss[0]) or self.isInteger(ss[0])
        return self.isInteger(ss[1]) and (self.isFloat(ss[0]) or self.isInteger(ss[0]))
# @lc code=end