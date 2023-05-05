#
# @lc app=leetcode.cn id=2432 lang=python3
#
# [2432] 处理用时最长的那个任务的员工
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        for i in reversed(range(1, len(logs))):
            logs[i][1] -= logs[i - 1][1]
        print(logs)
        return max(logs, key=lambda x:(x[1], -x[0]))[0]
# @lc code=end

print(Solution().hardestWorker(n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]))
print(Solution().hardestWorker(n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]))