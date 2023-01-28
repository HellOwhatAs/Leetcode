#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        state=[None,None]
        ret=0
        for i in range(len(nums)):
            if state[0]==nums[i]==state[1]:
                nums[i]=None
                ret+=1
            elif state[0]==nums[i]:
                state[1]=nums[i]
            else:
                state[0]=nums[i]
        for i in range(ret):nums.remove(None)
        return len(nums)
# @lc code=end

nums=[1,1,1,2,2,2,3,3]
l=Solution().removeDuplicates(nums)
print(nums[:l])