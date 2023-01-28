#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

# @lc code=start
class Solution:
    def judge(self,n:int):
        s=set(str(n))
        if '3' in s or '4' in s or '7' in s:return False
        if '2' in s or '5' in s or '6' in s or '9' in s:return True
        return False
    def rotatedDigits(self, n: int) -> int:
        ret=0
        for i in range(1,n+1):
            if self.judge(i):
                ret+=1
        return ret
# @lc code=end

s=Solution()
print(s.judge(2))