#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            s.append(s.pop()+s.pop()  if i=='+' else -s.pop()+s.pop() if i=='-' else s.pop()*s.pop()  if i=='*' else int(s.pop()**-1*s.pop()) if i=='/' else int(i))
        return s[0]
# @lc code=end

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))