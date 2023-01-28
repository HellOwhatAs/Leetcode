#
# @lc app=leetcode.cn id=816 lang=python3
#
# [816] 模糊坐标
#

# @lc code=start
from typing import List
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        ret=[]
        s=s[1:-1]
        for c in range(1,len(s)):
            l,r=s[:c],s[c:]
            ls,rs=[],[]
            if len(l)==1 or l[0]!='0':ls.append(l)
            if len(r)==1 or r[0]!='0':rs.append(r)
            for d in range(1,len(l)):
                l1,l2=l[:d],l[d:]
                if (len(l1)==1 or l1[0]!='0') and l2[-1]!='0':
                    ls.append(l1+'.'+l2)
            for d in range(1,len(r)):
                r1,r2=r[:d],r[d:]
                if (len(r1)==1 or r1[0]!='0') and r2[-1]!='0':
                    rs.append(r1+'.'+r2)
            for i in ls:
                for j in rs:
                    ret.append("({}, {})".format(i,j))
        return ret
# @lc code=end

print(Solution().ambiguousCoordinates("(100)"))