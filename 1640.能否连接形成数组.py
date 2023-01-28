#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#

# @lc code=start
from typing import List
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dd={i[0]:i for i in pieces}
        ss=0
        while ss<len(arr):
            if arr[ss] in dd:
                tmp=dd[arr[ss]]
                if tmp!=arr[ss:ss+len(tmp)]:
                    return False
                dd.pop(arr[ss])
                ss+=len(tmp)
            else:
                return False
        return True
# @lc code=end

