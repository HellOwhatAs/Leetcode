#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] 括号的分数
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for i in s:
            if i=='(':
                stack.append(i)
            else:
                tmp=0
                while stack[-1]!='(':
                    tmp+=stack.pop()
                stack[-1]=tmp*2 if tmp else 1
        return sum(stack)

                
# @lc code=end

print(Solution().scoreOfParentheses("(()(()))"))
