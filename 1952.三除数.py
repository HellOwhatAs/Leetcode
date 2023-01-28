#
# @lc app=leetcode.cn id=1952 lang=python3
#
# [1952] 三除数
#

# @lc code=start
class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                if count == 3: return False
                count += 1
        return count == 3
# @lc code=end

print(Solution().isThree(10**4))