#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
from typing import List
class Solution:
    def func(self,s:str,n:int)->List[str]:
        if not s:return
        if n==0:
            if s[0]=='0' and len(s)>1:return
            if int(s)<=255:yield s
            else:return 
        else:
            for i in self.func(s[1:],n-1):
                yield (s[0]+"."+i)
            if s[0]=='0':return
            for i in self.func(s[2:],n-1):
                yield (s[:2]+"."+i)
            if int(s[:3])<=255:
                for i in self.func(s[3:],n-1):
                    yield (s[:3]+"."+i)
    def restoreIpAddresses(self, s: str) -> List[str]:
        return list(self.func(s,3))
# @lc code=end

print(Solution().restoreIpAddresses("0000"))