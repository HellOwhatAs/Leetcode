#
# @lc app=leetcode.cn id=1255 lang=python3
#
# [1255] 得分最高的单词集合
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count_letters, n, ret = Counter(letters), len(words), 0
        for i in range(1 << n):
            str_tmp = "".join(word for idx, word in enumerate(words) if (i >> idx) & 1)
            if all(count_letters[k] >= v for k, v in Counter(str_tmp).items()):
                ret = max(ret, sum(score[ord(j) - ord('a')] for j in str_tmp))
        return ret

# @lc code=end

print(Solution().maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))
print(Solution().maxScoreWords(words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]))
print(Solution().maxScoreWords(words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]))