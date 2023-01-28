#
# @lc app=leetcode.cn id=2299 lang=python3
#
# [2299] 强密码检验器 II
#

# @lc code=start
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        return not (len(password)<8 or (not (any(chr(i) in (c:=__import__("collections").Counter(password)) for i in range(ord('a'), ord('z')+1)) and any(chr(i) in c for i in range(ord('A'), ord('Z')+1)) and any(chr(i) in c for i in range(ord('0'), ord('9')+1)) and any((i) in c for i in '!@#$%^&*()-+'))) or any(password[i-1] == password[i] for i in range(1, len(password))))
# @lc code=end

