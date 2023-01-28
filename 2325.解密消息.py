#
# @lc app=leetcode.cn id=2325 lang=python3
#
# [2325] 解密消息
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ktable, kidx = {' ': ' '}, ord('a') 
        for i in key:
            if not i in ktable:
                ktable[i] = chr(kidx)
                kidx += 1
        return "".join(ktable[i] for i in message) 
        
# @lc code=end

print(Solution().decodeMessage(key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))