#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [0] if not n else (tmp:=self.grayCode(n-1))+[i|(1<<(n-1)) for i in reversed(tmp)]
        
# @lc code=end

