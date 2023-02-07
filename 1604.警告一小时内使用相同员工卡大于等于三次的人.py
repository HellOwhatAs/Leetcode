#
# @lc app=leetcode.cn id=1604 lang=python3
#
# [1604] 警告一小时内使用相同员工卡大于等于三次的人
#

# @lc code=start
from typing import List
from itertools import groupby
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        return [i for i, it in groupby(sorted(zip(keyName, keyTime), key=lambda x:x[0]), key=lambda x:x[0]) if ((tmp:=sorted(int(j[1][:2]) * 60 + int(j[1][-2:]) for j in it)), any(tmp[k] - tmp[k - 2] <= 60 for k in range(2, len(tmp))))[1]]
# @lc code=end

print(Solution().alertNames(keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]))
print(Solution().alertNames(keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]))
print(Solution().alertNames(keyName = ["john","john","john"], keyTime = ["23:58","23:59","00:01"]))
print(Solution().alertNames(keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"], keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]))