#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
from typing import Union
def mycache(dd):
    def _mycache(func):
        def ret(self,a,b,c,d):
            if (a,b,c,d) in dd:return dd[(a,b,c,d)]
            dd[(a,b,c,d)]=func(self,a,b,c,d)
            return dd[(a,b,c,d)]
        return ret
    return _mycache
class Solution:
    dd={}
    @mycache(dd)
    def func(self,ss,se,ps,pe)->bool:
        if pe==ps:return se==ss
        first_matched=se>ss and (self.s[ss]==self.p[ps] or self.p[ps]=='.')
        if not first_matched:
            if pe-ps>=2 and self.p[ps+1]=='*':
                return self.func(ss,se,ps+2,pe)
            else:return False
        else:
            if pe-ps>=2 and self.p[ps+1]=='*':
                return self.func(ss+1,se,ps,pe) or self.func(ss,se,ps+2,pe)
            return self.func(ss+1,se,ps+1,pe)
    def isMatch(self, s: str, p: str) -> bool:
        self.s,self.p=s,p
        self.dd.clear()
        return self.func(0,len(s),0,len(p))
# @lc code=end

