#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#

# @lc code=start
from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack,left=[0],[1]
        for i in range(1,len(arr)):
            while stack and arr[stack[-1]]>=arr[i]:stack.pop()
            left.append(i-stack[-1] if stack else i+1),stack.append(i)
        arr.reverse()
        stack,right=[0],[1]
        for i in range(1,len(arr)):
            while stack and arr[stack[-1]]>arr[i]:stack.pop()
            right.append(i-stack[-1] if stack else i+1),stack.append(i)
        return sum(i*j*k for i,j,k in zip(reversed(left),right,arr))%(10**9 + 7)
# @lc code=end

print(Solution().sumSubarrayMins([71,55,82,55]))

"""
3 1 2 4
1 2 1 1
------
1 2 4
"""

"""
4 2 1 3
1 2 3 1
------
1 3
"""

"""
3 1 2 4
1 3 2 1
1 2 1 1
1 6 2 1
3 6 4 4
"""