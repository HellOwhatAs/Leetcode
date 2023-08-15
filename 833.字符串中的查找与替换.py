#
# @lc app=leetcode.cn id=833 lang=python3
#
# [833] 字符串中的查找与替换
#

# @lc code=start
from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        indices, sources, targets = zip(*sorted(zip(indices, sources, targets)))
        ss: List[str] = []
        pre = s[: indices[0]]
        for i in range(len(indices)):
            ss.append(s[indices[i]: (indices[i+1] if i+1 < len(indices) else None)])
        ret: List[str] = []
        for subs, source, target in zip(ss, sources, targets):
            if subs.startswith(source):
                ret.append(target + subs[len(source):])
            else:
                ret.append(subs)
        return pre + ''.join(ret)

# @lc code=end

print(Solution().findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]))