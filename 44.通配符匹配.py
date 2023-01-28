#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
def mycache(dd:dict):
    def _mycache(func):
        def ret(self,a,b):
            if (a,b) in dd:return dd[(a,b)]
            ret=func(self,a,b)
            dd[(a,b)]=ret
            return ret
        return ret
    return _mycache
class Solution:
    dd={}
    @mycache(dd)
    def func(self,ss:int,ps:int) -> bool:
        if self.pe==ps:return ss==self.se
        if ss==self.se:
            for i in range(ps,self.pe):
                if self.p[i]!='*':return False
            return True
        if self.p[ps]=='*':
            for i in range(ss,self.se+1):
                if self.func(i,ps+1):return True
            return False
        else:
            if self.s[ss]==self.p[ps] or self.p[ps]=='?':
                return self.func(ss+1,ps+1)
            else:return False
    def isMatch(self, s: str, p: str) -> bool:
        self.s,self.p=s,p
        self.se,self.pe=len(s),len(p)
        self.dd.clear()
        return self.func(0,0)
# @lc code=end
solu=Solution()
print(solu.isMatch("a"*200,"*a*"*10+"*"))
print(solu.dd)
