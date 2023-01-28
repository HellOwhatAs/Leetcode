#
# @lc app=leetcode.cn id=1487 lang=python3
#
# [1487] 保证文件名唯一
#

# @lc code=start
from typing import List
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d, ret = {}, []
        for name in names:
            if not name in d: 
                ret.append(name)
                d[name] = 1
            else:
                tmp = name+"({})".format(d[name])
                while tmp in d:
                    d[name] += 1
                    tmp = name+"({})".format(d[name])
                d[tmp] = 1
                ret.append(tmp)
        return ret
# @lc code=end

