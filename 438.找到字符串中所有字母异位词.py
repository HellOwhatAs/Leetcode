#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from typing import List, Optional

class Solution:

    @staticmethod
    def feature(s: str, _start: int = 0, _end: Optional[int] = None) -> List[int]:
        start, end = _start, len(s) if _end is None else _end
        ret = [0] * 26
        offset = ord('a')
        for i in range(start, end):
            ret[ord(s[i]) - offset] += 1
        return ret

    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenp = len(p)
        if len(s) < lenp: return []
        feature_p = self.feature(p)
        feature_s = self.feature(s, 0, lenp)
        ret: List[int] = []
        if feature_s == feature_p: ret.append(0)
        offset = ord('a')
        for i in range(1, len(s) - lenp + 1):
            feature_s[ord(s[i-1]) - offset] -= 1
            feature_s[ord(s[i+lenp-1]) - offset] += 1
            if feature_s == feature_p: ret.append(i)
        return ret

# @lc code=end

print(Solution().findAnagrams(s = "cbaebabacd", p = "abc"))
print(Solution().findAnagrams(s = "abab", p = "ab"))
print(Solution().findAnagrams("aaaaaaaaaa", "aaaaaaaaaaaaa"))