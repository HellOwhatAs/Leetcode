#
# @lc app=leetcode.cn id=2231 lang=python3
#
# [2231] 按奇偶性交换后的最大数字
#

# @lc code=start
class Solution:
    def largestInteger(self, num: int) -> int:
        oddval, oddidx, evenval, strnum, ret = [], set(), [], str(num), 0
        for ii, i in enumerate(map(int, strnum)):
            if i % 2:
                oddval.append(i)
                oddidx.add(ii)
            else:
                evenval.append(i)
        oddval.sort()
        evenval.sort()
        for i in range(len(strnum)):
            ret *= 10
            ret += oddval.pop() if i in oddidx else evenval.pop()
        return ret
        
# @lc code=end

print(Solution().largestInteger(65875))