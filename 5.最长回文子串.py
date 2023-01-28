#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
dpdp={}
def mycache(func):
    def ret(self,l:int,r:int)->bool:
        if (l,r) in dpdp:return dpdp[(l,r)]
        dpdp[(l,r)]=func(self,l,r)
        return dpdp[(l,r)]
    return ret
class Solution:
    @mycache
    def dp(self,l:int,r:int)->bool:
        if l==r:return 1
        if l+1==r:return self.s[l]==self.s[r]
        return self.s[l]==self.s[r] and self.dp(l+1,r-1)
    def longestPalindrome(self, s: str) -> str:
        if(len(set(s))==1):return s
        dpdp.clear()
        self.s=s
        max_len=0
        ret=(0,0)
        for i in range(len(s)):
            for j in range(i,len(s)):
                if(j-i+1>max_len and self.dp(i,j)):
                    max_len=j-i+1
                    ret=(i,j)
        return s[ret[0]:ret[1]+1]
# @lc code=end
