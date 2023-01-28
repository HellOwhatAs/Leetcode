#
# @lc app=leetcode.cn id=1652 lang=python3
#
# [1652] 拆炸弹
#

# @lc code=start
from typing import List
class Solution:
    def get(self,x:int)->int:
        return self.code[x%len(self.code)]
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:return [0]*len(code)
        self.code=code
        ret=[0]
        if k>0:
            for i in range(1,k+1):
                ret[-1]+=self.get(i)
            for i in range(1,len(code)):
                ret.append(ret[-1]-self.get(i)+self.get(i+k))
            return ret
        else:
            k=-k
            for i in range(1,k+1):
                ret[-1]+=self.get(-i)
            for i in range(1,len(code)):
                ret.append(ret[-1]+self.get(i-1)-self.get(i-k-1))
            return ret
# @lc code=end

print(Solution().decrypt([2,4,9,3], -2))