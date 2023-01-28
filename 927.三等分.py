#
# @lc app=leetcode.cn id=927 lang=python3
#
# [927] 三等分
#

# @lc code=start
from typing import List
class Solution:
    def ith_index(self,arr:List[int],val:int,i:int=0,start:int=0)->int:
        for _ in range(start,len(arr)):
            if arr[_]==val:
                if i==1:return _
                i-=1
        return -1
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n=arr.count(1)
        if not n:return[0,len(arr)-1]
        if n%3:return [-1,-1]
        a=self.ith_index(arr,1,n//3)
        b=self.ith_index(arr,1,n//3,a+1)
        c=self.ith_index(arr,1,n//3,b+1)
        end_zero=len(arr)-1-c
        ret1,ret2=a+end_zero,b+end_zero+1
        if ret1>=b or ret2>c:return [-1,-1]
        if int("".join(map(str,arr[:ret1+1])),base=2)==int("".join(map(str,arr[ret1+1:ret2])),base=2)==int("".join(map(str,arr[ret2:])),base=2):return [ret1,ret2]
        return [-1,-1]
        
# @lc code=end
print(Solution().threeEqualParts([1,1,1,1,1,1]))
