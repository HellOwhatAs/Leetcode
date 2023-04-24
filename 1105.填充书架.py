#
# @lc app=leetcode.cn id=1105 lang=python3
#
# [1105] 填充书架
#

# @lc code=start
from typing import List
class Solution:
    def func(self, start: int) -> int:
        if start in self.data: return self.data[start]
        width, height, ret = 0, 0, float('inf')
        for i in range(start, self.n):
            width += self.books[i][0]
            if width > self.width: break
            height = max(height, self.books[i][1])
            ret = min(ret, height + self.func(i + 1))
        ret = 0 if ret == float('inf') else ret
        self.data[start] = ret
        return ret
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        self.books, self.width, self.n = books, shelfWidth, len(books)
        self.data = {}
        return self.func(0)
# @lc code=end

print(Solution().minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4))
print(Solution().minHeightShelves(books = [[1,3],[2,4],[3,2]], shelfWidth = 6))