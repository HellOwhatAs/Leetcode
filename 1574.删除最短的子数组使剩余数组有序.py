#
# @lc app=leetcode.cn id=1574 lang=python3
#
# [1574] 删除最短的子数组使剩余数组有序
#

# @lc code=start
from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) == 1: return 0
        if len(arr) == 2: return int(arr[0] > arr[1])
        for l in range(len(arr) - 1):
            if arr[l + 1] < arr[l]: break
        for r in reversed(range(1, len(arr))):
            if arr[r - 1] > arr[r]: break
        if l >= r: return 0
        ans = len(arr) - 1
        j = r
        for i in range(l + 1):
            while j < len(arr) and arr[i] > arr[j]: j += 1
            ans = min(ans, j - i - 1)
        return min(ans, r, len(arr) - l - 1)

# @lc code=end

print(Solution().findLengthOfShortestSubarray(arr = [1,2,3,10,4,2,3,5]))
print(Solution().findLengthOfShortestSubarray(arr = [5,4,3,2,1]))
print(Solution().findLengthOfShortestSubarray(arr = [1,2,3]))
print(Solution().findLengthOfShortestSubarray(arr = [1]))

print(Solution().findLengthOfShortestSubarray([2,2,2,1,1,1]))