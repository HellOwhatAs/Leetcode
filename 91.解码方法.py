#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
def mycache(dd):
    def _mycache(func):
        def ret(self,x):
            if x in dd:return dd[x]
            tmp=func(self,x)
            dd[x]=tmp
            return tmp
        return ret
    return _mycache
class Solution:
    dd={}
    @mycache(dd)
    def func(self,ss:int)->bool:
        if self.s[ss]=='0':return 0
        if self.ls-ss==1:return 1
        elif self.ls-ss==2:return self.func(ss+1)+(int(self.s[ss:])<=26)
        else:
            ret=self.func(ss+1)
            if int(self.s[ss:ss+2])<=26:
                ret+=self.func(ss+2)
            return ret
    def numDecodings(self, s: str) -> int:
        self.dd.clear()
        self.s,self.ls=s,len(s)
        return self.func(0)
# @lc code=end

print(Solution().numDecodings("111111111111111111111111111111111111111111111"))