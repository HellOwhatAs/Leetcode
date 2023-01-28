#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#

# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if not word in sequence:return 0
        ret=1
        while True:
            if not word*(ret+1) in sequence:
                return ret
            ret+=1       
# @lc code=end

