#
# @lc app=leetcode.cn id=1053 lang=python3
#
# [1053] 交换一次的先前排列
#

# @lc code=start
from typing import List
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in reversed(range(n - 1)):
            if arr[i] > arr[i + 1]:
                j = n - 1
                while arr[j] >= arr[i] or arr[j] == arr[j - 1]:
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]
                break
        return arr
# @lc code=end

print(Solution().prevPermOpt1(arr = [3,2,1]))
print(Solution().prevPermOpt1(arr = [1,1,5]))
print(Solution().prevPermOpt1(arr = [1,9,4,6,7]))
print(Solution().prevPermOpt1([3,1,1,3]))