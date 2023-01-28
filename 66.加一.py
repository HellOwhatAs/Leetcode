#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        digits[-1]+=1
        while(digits[i]>9):
            digits[i]%=10
            i-=1
            if i<0:return [1]+digits
            digits[i]+=1
        return digits
# @lc code=end

