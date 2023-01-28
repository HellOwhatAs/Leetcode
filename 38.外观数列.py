#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:return "1"
        val=self.countAndSay(n-1)
        ret=[val[0]]
        d=[1]
        for i in range(1,len(val)):
            if val[i]==ret[-1]:
                d[-1]+=1
            else:
                ret.append(val[i])
                d.append(1)
        return "".join([str(c)+i for c,i in zip(d,ret)])
# @lc code=end

