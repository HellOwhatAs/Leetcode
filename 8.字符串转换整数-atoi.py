#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        try:
            ret=None
            for i in s:
                if ret is None:
                    if i=='+':ret=[]
                    elif i=='-':ret=['-']
                    elif i in "0123456789":ret=[i]
                    elif i==' ':continue
                    else:return 0
                else:
                    if i in "0123456789":ret.append(i)
                    else:break
            ret="".join(ret)
            return min(max(-2147483648,int(ret) if ret else 0),2147483647)
        except:
            return 0
# @lc code=end

